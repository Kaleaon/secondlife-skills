import os, re, xml.etree.ElementTree as ET, yaml
ROOT=os.path.dirname(os.path.abspath(__file__)); SRC=os.path.join(ROOT,"sources"); OUT=os.path.join(ROOT,"skills")
def w(skill,fname,text):
    d=os.path.join(OUT,skill,"references"); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,fname),"w").write(text); print(fname,len(text)); return len(text)
total=0
# Firestorm settings (same LLSD format)
def parse_settings(path):
    tree=ET.parse(path); rootmap=tree.getroot(); firstmap=rootmap.find("map"); kids=list(firstmap); settings={}
    for i in range(0,len(kids)-1,2):
        if kids[i].tag!="key": continue
        name=kids[i].text; valmap=kids[i+1]; fields={}; vk=list(valmap)
        for j in range(0,len(vk)-1,2):
            if vk[j].tag=="key":
                v=vk[j+1]; fields[vk[j].text]=(v.text or "") if len(v)==0 else " ".join((c.text or "") for c in v.iter() if c is not v)
        settings[name]=fields
    return settings
try:
    fs=parse_settings(os.path.join(SRC,"firestorm-settings.xml"))
    out=["# Firestorm Settings Reference (generated from FirestormViewer/phoenix-firestorm)\n",
    f"Generated from Firestorm's `indra/newview/app_settings/settings.xml` ({len(fs)} settings). Firestorm adds many settings the official viewer does not have and changes some defaults. When code or advice depends on a setting, check whether the name exists in the official viewer reference too, and state which viewer you mean.\n"]
    for name in sorted(fs):
        f=fs[name]
        out.append(f"\n## {name}\n")
        out.append(f"- Type: {f.get('Type','?')} | Default value: `{f.get('Value','')}` | Persisted: {f.get('Persist','?')}\n")
        if f.get("Comment"): out.append(f"- Comment: {f['Comment']}\n")
    total+=w("secondlife_viewer_cpp","firestorm-settings.md","\n".join(out))
except Exception as e: print("fs settings fail", e)

# OpenSim extra configs from extracted source
OS=os.path.join(SRC,"opensim-src","bin")
import glob
for cfg in sorted(glob.glob(os.path.join(OS,"**","*.ini.example"), recursive=True)+glob.glob(os.path.join(OS,"**","*.ini"), recursive=True)):
    base=os.path.basename(cfg)
    if base in ("OpenSim.ini.example","Robust.ini.example"): continue
    raw=open(cfg,encoding="utf-8",errors="replace").read()
    if len(raw)<500: continue
    out=[f"# OpenSim Config: {base} (from opensim/opensim)\n","Structured from the stock file in the OpenSim repo (BSD). Comments are upstream's own.\n"]
    for line in raw.splitlines():
        s=line.strip(); m=re.match(r'^\[(.+)\]$', s)
        if m: out.append(f"\n## [{m.group(1)}]\n"); continue
        if s.startswith(";") or s.startswith("#"):
            if len(s)>2: out.append(f"{s.lstrip(';# ')}\n")
        elif "=" in s:
            k,v=s.split("=",1); out.append(f"- `{k.strip()}` = `{v.strip()}`\n")
    total+=w("secondlife_opensim_server", "config-"+base.replace(".example","").lower().replace(".","-")+".md","\n".join(out))

# LSL worked call patterns per function
d=yaml.safe_load(open(os.path.join(SRC,"lsl_definitions.yaml"))); funcs=d.get("functions",{})
out=["# LSL Function Call Patterns (generated from secondlife/lsl-definitions)\n",
"For every LSL function: the canonical signature, a minimal call pattern built from its real argument names and types, its return handling, and its cost fields. Patterns are illustrative skeletons, combine them with the full examples in examples-lsl.md and the purpose text in lsl-functions.md.\n"]
place={"integer":"42","float":"1.0","string":"\"text\"","key":"llGetOwner()","vector":"<1.0, 0.0, 0.0>","rotation":"ZERO_ROTATION","list":"[1, 2, 3]"}
for name in sorted(funcs):
    e=funcs[name] or {}; args=[]
    for a in e.get("arguments",[]) or []:
        for an,av in a.items(): args.append((an,av.get("type","?")))
    callargs=", ".join(place.get(t, an) if False else f"{an}" for an,t in args)
    out.append(f"\n## {name}\n")
    out.append(f"```lsl\n// {e.get('tooltip','')}\n")
    if e.get("return") and e["return"]!="void":
        out.append(f"{e['return']} result = {name}({callargs});\n")
    else:
        out.append(f"{name}({callargs});\n")
    out.append("```\n")
    if args: out.append("- Arguments: "+", ".join(f"`{an}` ({t})" for an,t in args)+"\n")
    out.append(f"- Returns: {e.get('return','void')} | Energy: {e.get('energy','n/a')} | Sleep: {e.get('sleep',0)} s | Categories: {', '.join(e.get('categories',[]) or [])}\n")
    if e.get("sleep",0): out.append(f"- Delay: budget {e['sleep']} s of script stall per call in event handlers.\n")
total+=w("secondlife_lsl_scripting","lsl-call-patterns.md","\n".join(out))
print("TOTAL4", total)
