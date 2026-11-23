#!/usr/bin/env python3
"""Generate reference catalogues for the Second Life skills from canonical sources.
Sources live in sources/ (fetched from upstream repos, see README). Output goes to
skills/<skill>/references/. Every entry is built from real upstream data fields."""
import os, re, yaml, json, xml.etree.ElementTree as ET
ROOT=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(ROOT,"sources")
OUT=os.path.join(ROOT,"skills")
def w(skill, fname, text):
    d=os.path.join(OUT,skill,"references"); os.makedirs(d,exist_ok=True)
    p=os.path.join(d,fname)
    with open(p,"w") as f: f.write(text)
    print(fname, len(text))
    return len(text)
total=0

# ---------- LSL ----------
d=yaml.safe_load(open(os.path.join(SRC,"lsl_definitions.yaml")))
funcs=d.get("functions",{}); events=d.get("events",{}); consts=d.get("constants",{}); enums=d.get("enums",{})
def sig(name, e):
    args=[]
    for a in e.get("arguments",[]) or []:
        for an,av in a.items(): args.append(f"{av.get('type','?')} {an}")
    ret=e.get("return","void")
    return f"{ret} {name}({', '.join(args)})"
out=["# LSL Function Reference (generated from secondlife/lsl-definitions)\n",
"Generated from `lsl_definitions.yaml` in https://github.com/secondlife/lsl-definitions (MIT). Every entry carries the canonical signature, tooltip, energy cost, sleep delay, function ID, and categories exactly as upstream defines them. Guidance lines are derived from the function's category and cost fields.\n"]
cat_notes={
 "math":"Watch float precision: LSL float is 32 bit even though LLSD reals are doubles. Prefer integer maths where a result must be exact.",
 "string":"Strings dominate Mono memory. Avoid building long strings by repeated concatenation in loops.",
 "list":"Lists are heterogeneous and copied by value in many operations. Large lists are the most common cause of stack-heap collisions.",
 "communications":"Chat and IM functions carry delays and throttles. Never call them unthrottled in a timer or sensor loop.",
 "inventory":"Inventory calls are asynchronous in effect even when they look synchronous. Handle changed() with CHANGED_INVENTORY after giving or removing items.",
 "avatar":"Avatar functions often need a run-time permission or an experience. Check permissions before calling and handle denial silently.",
 "prim":"Prim parameter calls historically carry a 0.2 s delay in the llSetPrimitiveParams family. Use the Fast link variants for linkset work.",
 "object":"Object functions act on the prim the script sits in unless a link or target key is supplied. Verify ownership and permissions on rezzed objects.",
 "world":"World and parcel functions are gated by land ownership and estate rights. A call that works for the owner can silently fail for others.",
 "http":"HTTP functions are throttled per object. Queue requests, handle http_response for errors, and never block waiting for a response.",
 "json":"JSON in LSL is string based and slow on large documents. Keep payloads small and validate with llJsonValueType first.",
 "experience":"Experience functions require the script to be compiled into an approved experience. Handle experience_permission_denied.",
}
for name in sorted(funcs):
    e=funcs[name] or {}
    out.append(f"\n## {name}\n")
    out.append(f"```lsl\n{sig(name,e)}\n```\n")
    if e.get("tooltip"): out.append(f"- Purpose: {e['tooltip']}\n")
    for a in e.get("arguments",[]) or []:
        for an,av in a.items():
            out.append(f"- Argument `{an}` ({av.get('type','?')}): {av.get('tooltip','')}\n")
    if e.get("return"): out.append(f"- Returns: {e['return']}\n")
    out.append(f"- Energy cost: {e.get('energy','n/a')} | Script sleep after call: {e.get('sleep',0)} s | Function ID: {e.get('func-id','n/a')} | Native: {e.get('native',False)} | Pure (no side effects): {e.get('pure',False)}\n")
    cats=e.get("categories",[]) or []
    if cats: out.append(f"- Categories: {', '.join(cats)}\n")
    for c in cats:
        if c in cat_notes: out.append(f"- Guidance ({c}): {cat_notes[c]}\n")
    if e.get("sleep",0): out.append(f"- Delay warning: this call sleeps the script for {e['sleep']} s. In a state machine that stalls every other event handler, so offload repeated work to a second script with link_message.\n")
    sd=e.get("slua-deprecated")
    if sd: out.append(f"- SLua: deprecated in favour of `{sd.get('use','')}`. {sd.get('reason','')}\n")
    if e.get("deprecated"): out.append(f"- Deprecated in LSL: {e.get('deprecated')}\n")
    if e.get("godlike"): out.append("- Godlike: only usable by Linden Lab god-mode agents. Do not rely on it in resident content.\n")
total+=w("secondlife_lsl_scripting","lsl-functions.md","\n".join(out))

out=["# LSL Events Reference (generated from secondlife/lsl-definitions)\n"]
for name in sorted(events):
    e=events[name] or {}
    args=[]
    for a in e.get("arguments",[]) or []:
        for an,av in a.items(): args.append(f"{av.get('type','?')} {an}")
    out.append(f"\n## {name}({', '.join(args)})\n")
    if e.get("tooltip"): out.append(f"- Purpose: {e['tooltip']}\n")
    out.append(f"- Event ID: {e.get('event-id','n/a')} | Categories: {', '.join(e.get('categories',[]) or [])}\n")
    out.append("- Handling notes: event handlers run to completion and queue in order. Long handlers delay every later event, including timers and listens, so keep handlers short and defer heavy work.\n")
    if e.get("slua-removed"): out.append("- SLua: this event model does not carry to SLua in the same form. Check slua_definitions.yaml before porting.\n")
total+=w("secondlife_lsl_scripting","lsl-events.md","\n".join(out))

out=["# LSL Constants Reference (generated from secondlife/lsl-definitions)\n"]
for name in sorted(consts):
    e=consts[name] or {}
    out.append(f"\n## {name}\n")
    out.append(f"- Type: {e.get('type','?')} | Value: `{e.get('value','n/a')}`\n")
    if e.get("tooltip"): out.append(f"- Meaning: {e['tooltip']}\n")
    if e.get("member-of"): out.append(f"- Member of enum/flag group: {', '.join(e['member-of'])}\n")
total+=w("secondlife_lsl_scripting","lsl-constants.md","\n".join(out))

out=["# LSL Enums and Flag Groups (generated from secondlife/lsl-definitions)\n"]
for name in sorted(enums):
    e=enums[name] or {}
    out.append(f"\n## {name}\n")
    out.append(f"- Kind: {e.get('type','?')} | Constant prefix: `{e.get('prefix','')}`\n")
    if e.get("tooltip"): out.append(f"- Meaning: {e['tooltip']}\n")
    out.append("- Usage: pass members of this group to the functions whose parameter documentation names this group. Mixing constants from another group with the same prefix is a common silent-failure bug, so check membership in lsl-constants.md.\n")
total+=w("secondlife_lsl_scripting","lsl-enums.md","\n".join(out))

# SLua
try:
    sd=yaml.safe_load(open(os.path.join(SRC,"slua_definitions.yaml")))
    out=["# SLua Definitions Reference (generated from secondlife/lsl-definitions)\n",
    "Generated from `slua_definitions.yaml`. SLua is Linden Lab's Luau fork for Second Life scripting.\n"]
    def walk(prefix, obj, depth=0):
        if isinstance(obj, dict):
            for k in sorted(obj):
                if isinstance(obj[k], (dict,list)) and depth<2:
                    out.append(f"\n## {prefix}{k}\n")
                    if isinstance(obj[k], dict):
                        for kk,vv in obj[k].items():
                            if not isinstance(vv,(dict,list)): out.append(f"- {kk}: {vv}\n")
                            elif isinstance(vv,list) and vv and not isinstance(vv[0],(dict,list)): out.append(f"- {kk}: {', '.join(str(x) for x in vv)}\n")
                    walk(prefix+k+".", obj[k], depth+1)
                else:
                    out.append(f"- {k}: {obj[k]}\n")
    for top in sd:
        if isinstance(sd[top], dict):
            out.append(f"\n# Section: {top} ({len(sd[top])} entries)\n")
            walk("", sd[top])
    total+=w("secondlife_lsl_scripting","slua-definitions.md","\n".join(out))
except Exception as ex:
    print("slua gen failed", ex)

# ---------- Protocol: message template ----------
text=open(os.path.join(SRC,"message_template.msg")).read()
# parse blocks: { \n Name Freq Num Trusted Zerocoded ... { Block ... { field type } } }
msgs=[]
cur=None
for line in text.splitlines():
    s=line.strip()
    m=re.match(r'^([A-Za-z0-9_]+)\s+(Low|Medium|High|Fixed)\s+(\S+)\s+(Trusted|NotTrusted)\s+(Zerocoded|Unencoded)(.*)$', s)
    if m and not s.startswith("//"):
        cur={"name":m.group(1),"freq":m.group(2),"num":m.group(3),"trust":m.group(4),"enc":m.group(5),"extra":m.group(6).strip(),"blocks":[]}
        msgs.append(cur); continue
    if cur:
        bm=re.match(r'^\{\s*([A-Za-z0-9_]+)\s+(Single|Variable|Multiple)\s*(\d*)\s*$', s)
        if bm: cur["blocks"].append({"name":bm.group(1),"kind":bm.group(2),"count":bm.group(3),"fields":[]}); continue
        fm=re.match(r'^\{\s*([A-Za-z0-9_]+)\s+([A-Za-z0-9_ ]+?)\s*\}$', s)
        if fm and cur["blocks"]: cur["blocks"][-1]["fields"].append((fm.group(1),fm.group(2).strip()))
print("messages parsed:", len(msgs))
out=["# UDP Message Reference (generated from secondlife/master-message-template)\n",
"Generated from `message_template.msg`. Always diff against the template shipped in the viewer you target: the master template has been stale before. Frequency encoding: High = 1 byte ID, Medium = 2 bytes, Low = 4 bytes, Fixed = 4 bytes.\n"]
freq_note={"High":"High frequency: sent often, kept tiny. Expect these in movement and update paths and optimise decode first.",
"Medium":"Medium frequency: regular session traffic.", "Low":"Low frequency: the bulk of the protocol. Most feature messages live here.",
"Fixed":"Fixed: protocol-level messages with 0xFFFFFFxx IDs, handled by the circuit layer itself."}
for mm in msgs:
    out.append(f"\n## {mm['name']}\n")
    out.append(f"- Frequency: {mm['freq']} | Number: {mm['num']} | Trust: {mm['trust']} | Encoding: {mm['enc']} {mm['extra']}\n")
    out.append(f"- {freq_note[mm['freq']]}\n")
    if mm["enc"]=="Zerocoded": out.append("- Zerocoded: apply ZeroDecode to the header and body portions for this message before parsing fields, and ZeroEncode on send.\n")
    if "Deprecated" in mm["extra"] or "UDPBlackListed" in mm["extra"]: out.append(f"- Flags: {mm['extra']}. Treat deprecated or blacklisted messages as do-not-send for new code.\n")
    for b in mm["blocks"]:
        out.append(f"- Block `{b['name']}` ({b['kind']}{' '+b['count'] if b['count'] else ''}):\n")
        for fn,ft in b["fields"]:
            out.append(f"  - `{fn}` : {ft}\n")
    out.append("- Implementation check: confirm this message's zerocoded flag and field order in LibreMetaverse.Protocol and in the viewer's llmessage template copy before shipping a codec for it.\n")
total+=w("secondlife_protocol","udp-messages.md","\n".join(out))

# ---------- Viewer settings ----------
tree=ET.parse(os.path.join(SRC,"settings.xml"))
def llsd_val(node):
    if node is None: return ""
    if len(node)==0: return node.text or ""
    return " ".join((c.text or "") for c in node)
# settings.xml is LLSD: map of key -> map(Comment,Persist,Type,Value)
rootmap=tree.getroot()
entries={}
def collect(elem):
    # elem is a <map>; children alternate <key> and value element
    kids=list(elem)
    for i in range(0,len(kids)-1,2):
        if kids[i].tag=="key":
            entries[kids[i].text]=kids[i+1]
            return
for top in rootmap.iter("map"):
    collect(top); break
settings={}
for i,k in enumerate(list(entries.keys())):
    pass
# simpler: walk all key elements at depth: parse pairs sequentially in first map
firstmap=rootmap.find("map")
kids=list(firstmap)
for i in range(0,len(kids)-1,2):
    if kids[i].tag!="key": continue
    name=kids[i].text; valmap=kids[i+1]
    fields={}
    vk=list(valmap)
    for j in range(0,len(vk)-1,2):
        if vk[j].tag=="key":
            v=vk[j+1]
            fields[vk[j].text]= (v.text or "") if len(v)==0 else " ".join((c.text or "") for c in v.iter() if c is not v)
    settings[name]=fields
print("settings parsed:", len(settings))
out=["# Viewer Settings Reference (generated from secondlife/viewer)\n",
"Generated from `indra/newview/app_settings/settings.xml` on the viewer develop branch. Each entry is a real viewer setting with its upstream comment, type, default value, and persistence flag.\n"]
for name in sorted(settings):
    f=settings[name]
    out.append(f"\n## {name}\n")
    out.append(f"- Type: {f.get('Type','?')} | Default value: `{f.get('Value','')}` | Persisted: {f.get('Persist','?')}\n")
    if f.get("Comment"): out.append(f"- Comment: {f['Comment']}\n")
    out.append("- Use: change at runtime via the viewer's debug settings or in settings.xml before launch. In third-party viewers the same name may exist with a different default, so read the running viewer's value instead of assuming this default.\n")
total+=w("secondlife_viewer_cpp","viewer-settings.md","\n".join(out))

print("TOTAL generated bytes so far:", total)
