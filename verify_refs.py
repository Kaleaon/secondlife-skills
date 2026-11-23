#!/usr/bin/env python3
"""Verify every converted reference in the secondlife-skills repo:
frontmatter/YAML validity, markdown fence balance, JSON block validity,
and entry counts cross-checked against the canonical sources in sources/."""
import os, re, sys, json
ROOT=os.path.dirname(os.path.abspath(__file__)); SK=os.path.join(ROOT,"skills"); SRC=os.path.join(ROOT,"sources")
fails=[]; oks=[]
def ok(name,cond,detail=""):
    (oks if cond else fails).append(f"{name} {detail}")
    if not cond: print("FAIL:",name,detail)

# 1. SKILL.md frontmatter + skill.yaml
import yaml
for skill in sorted(os.listdir(SK)):
    d=os.path.join(SK,skill)
    if not os.path.isdir(d): continue
    txt=open(os.path.join(d,"SKILL.md"),encoding="utf-8").read()
    m=re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    ok(f"{skill} frontmatter", bool(m))
    if m:
        fm=yaml.safe_load(m.group(1))
        ok(f"{skill} frontmatter name", fm.get("name")==skill, str(fm.get("name")))
        ok(f"{skill} frontmatter desc", len(fm.get("description",""))>20)
    y=yaml.safe_load(open(os.path.join(d,"skill.yaml"),encoding="utf-8"))
    ok(f"{skill} skill.yaml parses", isinstance(y,dict))

# 2. All markdown: UTF-8, no NUL, balanced fences
nfiles=0
for dp,dn,fn in os.walk(SK):
    for f in fn:
        if not f.endswith(".md"): continue
        p=os.path.join(dp,f); raw=open(p,"rb").read(); nfiles+=1
        ok(f"{p} utf8", True)
        try: t=raw.decode("utf-8")
        except Exception as e: ok(f"{p} utf8", False, str(e)); continue
        ok(f"{f} no NUL", b"\x00" not in raw)
        fences=len(re.findall(r"^```", t, re.M))
        ok(f"{f} fences balanced", fences%2==0, f"({fences} fence lines)")
print(f"markdown files checked: {nfiles}")

# 3. LSL complete dump: JSON blocks parse + counts vs YAML
defs=yaml.safe_load(open(os.path.join(SRC,"lsl_definitions.yaml")))
comp=open(os.path.join(SK,"secondlife_lsl_scripting","references","lsl-definitions-complete.md"),encoding="utf-8").read()
blocks=re.findall(r"```json\n(.*?)```", comp, re.S)
bad=0
for b in blocks:
    try: json.loads(b)
    except Exception: bad+=1
ok("lsl-definitions-complete JSON blocks", bad==0, f"({len(blocks)} blocks, {bad} bad)")
expect=sum(len(v) for k,v in defs.items() if isinstance(v,dict))
ok("lsl-definitions-complete entry count", len(blocks)==expect, f"({len(blocks)} vs yaml {expect})")

# 4. LSL functions/constants counts
lf=open(os.path.join(SK,"secondlife_lsl_scripting","references","lsl-functions.md"),encoding="utf-8").read()
nf=lf.count("\n## ll")
ok("lsl-functions count", nf==len(defs["functions"]), f"({nf} vs {len(defs['functions'])})")
lc=open(os.path.join(SK,"secondlife_lsl_scripting","references","lsl-constants.md"),encoding="utf-8").read()
nc=lc.count("\n## ")
ok("lsl-constants count", nc>=len(defs["constants"]), f"({nc} vs {len(defs['constants'])})")

# 5. Message template: messages + stubs
tmpl=open(os.path.join(SRC,"message_template.msg")).read()
msgs=re.findall(r"^\s*([A-Za-z0-9_]+)\s+(Low|Medium|High|Fixed)\s+\S+\s+(Trusted|NotTrusted)\s+(Zerocoded|Unencoded)", tmpl, re.M)
ok("template messages parsed", len(msgs)==483, f"({len(msgs)})")
for lang in ["typescript","kotlin","rust","csharp"]:
    st=open(os.path.join(SK,"secondlife_protocol","references",f"message-stubs-{lang}.md"),encoding="utf-8").read()
    n=st.count("\n## ")
    ok(f"stubs-{lang} count", n==483, f"({n})")
udp=open(os.path.join(SK,"secondlife_protocol","references","udp-messages.md"),encoding="utf-8").read()
ok("udp-messages count", udp.count("\n## ")>=483, f"({udp.count(chr(10)+'## ')})")

# 6. Viewer + Firestorm settings counts vs XML
import xml.etree.ElementTree as ET
for srcf, reff, label in [("settings.xml","viewer-settings.md","viewer"),("firestorm-settings.xml","firestorm-settings.md","firestorm")]:
    try:
        tree=ET.parse(os.path.join(SRC,srcf)); _m=tree.getroot().find("map"); n=len([c for c in _m if c.tag=="key"]) if _m is not None else -1
    except Exception as e:
        n=-1; print("settings xml parse issue", label, e)
    ref=open(os.path.join(SK,"secondlife_viewer_cpp","references",reff),encoding="utf-8").read()
    rn=ref.count("\n## ")
    ok(f"{label} settings entries", rn==n, f"(ref {rn} vs xml root settings {n})")

# 7. Code files: language markers
checks={
 ("secondlife_protocol","code-rust.md"):["ZeroDecode","Circuit","LLSD","Cargo.toml"],
 ("secondlife_protocol","code-go.md"):["package","ZeroDecode","Circuit"],
 ("secondlife_protocol","code-python.md"):["zerocode","class","LLSD"],
 ("secondlife_client_libraries","code-react-typescript.md"):["useEventQueue","LLSD","Circuit"],
 ("secondlife_client_libraries","code-kotlin.md"):["LLSD","Circuit","suspend"],
 ("secondlife_client_libraries","code-java-cpp.md"):["CMakeLists","LLSD"],
 ("secondlife_client_libraries","code-csharp.md"):["GridClient","LibreMetaverse"],
}
for (skill,f),marks in checks.items():
    t=open(os.path.join(SK,skill,"references",f),encoding="utf-8").read()
    for mk in marks: ok(f"{f} contains {mk}", mk in t)
    ok(f"{f} size>50KB", len(t)>50000, f"({len(t)})")

# 8. Examples counts
el=open(os.path.join(SK,"secondlife_lsl_scripting","references","examples-lsl.md"),encoding="utf-8").read()
ok("examples-lsl state_entry scripts", el.count("state_entry")>=25, f"({el.count('state_entry')})")
ec=open(os.path.join(SK,"secondlife_client_libraries","references","examples-clients.md"),encoding="utf-8").read()
ok("examples-clients size", len(ec)>90000, f"({len(ec)})")

# 9. Catalogues spot checks
api=open(os.path.join(SK,"secondlife_opensim_server","references","opensim-api.md"),encoding="utf-8").read()
ok("opensim-api size>1MB", len(api)>1000000, f"({len(api)})")
dm=open(os.path.join(SK,"secondlife_client_libraries","references","libremetaverse-data-model.md"),encoding="utf-8").read()
ok("libremetaverse-data-model has OSDMap or UUID types", ("UUID" in dm and len(dm)>50000), f"({len(dm)})")
caps=open(os.path.join(SK,"secondlife_protocol","references","capabilities.md"),encoding="utf-8").read()
ok("capabilities covers EventQueueGet+GetTexture", all(x in caps for x in ["EventQueueGet","GetTexture","FetchInventory2"]))

# 10. Master index sizes match disk
idx=open(os.path.join(SK,"secondlife_development","references","master-index.md"),encoding="utf-8").read()
mism=0; checked=0
for mm in re.finditer(r"`(skills/[^`]+)` — ([\d,]+) bytes", idx):
    p=os.path.join(ROOT,mm.group(1)); want=int(mm.group(2).replace(",",""))
    if os.path.exists(p):
        checked+=1
        if abs(os.path.getsize(p)-want)>2000: mism+=1
ok("master-index sizes", mism==0, f"({checked} checked, {mism} stale)")

print(f"\nPASS {len(oks)} checks, FAIL {len(fails)}")
for f in fails: print(" -", f)
sys.exit(1 if fails else 0)
