import os, re
ROOT=os.path.dirname(os.path.abspath(__file__)); SRC=os.path.join(ROOT,"sources"); OUT=os.path.join(ROOT,"skills")
def w(skill,fname,text):
    d=os.path.join(OUT,skill,"references"); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,fname),"w").write(text); print(fname,len(text)); return len(text)
total=0
LIB=os.path.join(SRC,"libre")
# Data model catalogue: every public type in Protocol + Types + Assets with its public fields
out=["# LibreMetaverse Data Model Reference (generated from cinderblocks/libremetaverse)\n",
"Every public class, struct, record, and enum in LibreMetaverse.Protocol, LibreMetaverse.Types, and LibreMetaverse.Assets, with its public fields. This is the data model a port must reproduce: packet records, login data, asset types, prim and inventory structures.\n"]
count=0
for proj in ["LibreMetaverse.Protocol","LibreMetaverse.Types","LibreMetaverse.Assets"]:
    base=os.path.join(LIB,proj)
    for dp,dn,fn in os.walk(base):
        if any(x in dp for x in ["obj","bin"]): continue
        for f in sorted(fn):
            if not f.endswith(".cs"): continue
            fp=os.path.join(dp,f); src=open(fp,encoding="utf-8",errors="replace").read()
            # find type blocks crudely: public (class|struct|record|enum) Name { ... balanced-ish up to 400 lines }
            for m in re.finditer(r'public\s+(?:static\s+|abstract\s+|sealed\s+|partial\s+)*(class|struct|record|enum)\s+(\w+)', src):
                kind,name=m.group(1),m.group(2)
                seg=src[m.end():m.end()+6000]
                fields=re.findall(r'public\s+(?:static\s+|readonly\s+|const\s+)*([\w<>\[\]\?,\.]+)\s+(\w+)\s*(?:[=;{])', seg[:seg.find("\n    }\n") if "\n    }\n" in seg else len(seg)])
                out.append(f"\n## {name} ({kind}) — {os.path.relpath(fp,LIB)}\n")
                seen=set()
                for ft,fnn in fields:
                    if fnn in seen or fnn==name: continue
                    seen.add(fnn); out.append(f"- `{ft} {fnn}`\n")
                count+=1
out.insert(2,f"Types catalogued: {count}.\n")
total+=w("secondlife_client_libraries","libremetaverse-data-model.md","\n".join(out))

# OpenSim console commands
OS=os.path.join(SRC,"opensim-src")
cmds={}
for dp,dn,fn in os.walk(OS):
    for f in fn:
        if not f.endswith(".cs"): continue
        fp=os.path.join(dp,f); src=open(fp,encoding="utf-8",errors="replace").read()
        for m in re.finditer(r'AddCommand\([^,]+,\s*this,\s*"([^"]+)",\s*"([^"]*)"', src):
            cmds[m.group(1)]=(m.group(2), os.path.relpath(fp,OS))
        for m in re.finditer(r'AddCommand\("([^"]+)",\s*"([^"]*)"', src):
            cmds.setdefault(m.group(1),(m.group(2), os.path.relpath(fp,OS)))
out=["# OpenSim Console Commands Reference (generated from opensim/opensim source)\n",
f"Extracted {len(cmds)} console commands registered in the OpenSim source, with their registered help text and the file that registers them. Run them from the region console or the ROBUST console as noted by the registering module.\n"]
for c in sorted(cmds):
    helptext, f = cmds[c]
    out.append(f"\n## {c}\n")
    out.append(f"- Help: {helptext}\n")
    out.append(f"- Registered in: `{f}`\n")
total+=w("secondlife_opensim_server","opensim-console-commands.md","\n".join(out))
print("TOTAL5", total)
