import os
ROOT=os.path.dirname(os.path.abspath(__file__)); SRC=os.path.join(ROOT,"sources"); OUT=os.path.join(ROOT,"skills")
def w(skill,fname,text):
    d=os.path.join(OUT,skill,"references"); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,fname),"w").write(text); print(fname,len(text)); return len(text)
total=0
for repo,branch,skill,fname,title in [
 ("secondlife/viewer","develop","secondlife_viewer_cpp","viewer-source-tree.md","Official Viewer Source Tree"),
 ("FirestormViewer/phoenix-firestorm","master","secondlife_viewer_cpp","firestorm-source-tree.md","Firestorm Source Tree"),
 ("AlchemyViewer/Alchemy","develop","secondlife_viewer_cpp","alchemy-source-tree.md","Alchemy Source Tree")]:
    tf=os.path.join(SRC, fname.split("-")[0]+"-tree.txt")
    if not os.path.exists(tf): print("missing",tf); continue
    paths=[l.strip() for l in open(tf) if l.strip()]
    out=[f"# {title} (generated from {repo} @{branch})\n",
    f"Complete file index of https://github.com/{repo} ({len(paths)} files). Use it to locate the exact file for a subsystem before fetching or cloning it. Paths are grouped by directory.\n"]
    from collections import defaultdict
    by=defaultdict(list)
    for p in paths: by[os.path.dirname(p) or "."].append(os.path.basename(p))
    for d in sorted(by):
        out.append(f"\n## {d}/ ({len(by[d])} files)\n")
        for f in sorted(by[d]): out.append(f"- `{f}`\n")
    total+=w(skill,fname,"\n".join(out))
print("TOTAL3",total)
