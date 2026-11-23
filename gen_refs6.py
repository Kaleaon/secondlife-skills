import os, re
ROOT=os.path.dirname(os.path.abspath(__file__)); SRC=os.path.join(ROOT,"sources"); OUT=os.path.join(ROOT,"skills")
def w(skill,fname,text):
    d=os.path.join(OUT,skill,"references"); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,fname),"w").write(text); print(fname,len(text)); return len(text)
text=open(os.path.join(SRC,"message_template.msg")).read()
msgs=[]; cur=None
for line in text.splitlines():
    s=line.strip()
    m=re.match(r'^([A-Za-z0-9_]+)\s+(Low|Medium|High|Fixed)\s+(\S+)\s+(Trusted|NotTrusted)\s+(Zerocoded|Unencoded)(.*)$', s)
    if m:
        cur={"name":m.group(1),"freq":m.group(2),"num":m.group(3),"trust":m.group(4),"enc":m.group(5),"blocks":[]}; msgs.append(cur); continue
    if cur:
        bm=re.match(r'^\{\s*([A-Za-z0-9_]+)\s+(Single|Variable|Multiple)\s*(\d*)\s*$', s)
        if bm: cur["blocks"].append({"name":bm.group(1),"kind":bm.group(2),"count":bm.group(3),"fields":[]}); continue
        fm=re.match(r'^\{\s*([A-Za-z0-9_]+)\s+([A-Za-z0-9_ ]+?)\s*\}$', s)
        if fm and cur["blocks"]: cur["blocks"][-1]["fields"].append((fm.group(1),fm.group(2).strip()))
print("messages:", len(msgs))
tsmap={"U8":"number","U16":"number","U32":"number","U64":"bigint","S8":"number","S16":"number","S32":"number","S64":"bigint","F32":"number","F64":"number","LLUUID":"UUID","LLVector3":"Vector3","LLVector3d":"Vector3d","LLVector4":"Vector4","LLQuaternion":"Quaternion","BOOL":"boolean","Variable 1":"Uint8Array","Variable 2":"Uint8Array","Fixed":"Uint8Array","IPADDR":"string","IPPORT":"number"}
ktmap={"U8":"UByte","U16":"UShort","U32":"UInt","U64":"ULong","S8":"Byte","S16":"Short","S32":"Int","S64":"Long","F32":"Float","F64":"Double","LLUUID":"UUID","LLVector3":"Vector3","LLVector3d":"Vector3d","LLVector4":"Vector4","LLQuaternion":"Quaternion","BOOL":"Boolean","Variable 1":"ByteArray","Variable 2":"ByteArray","Fixed":"ByteArray","IPADDR":"InetAddress","IPPORT":"Int"}
rsmap={"U8":"u8","U16":"u16","U32":"u32","U64":"u64","S8":"i8","S16":"i16","S32":"i32","S64":"i64","F32":"f32","F64":"f64","LLUUID":"Uuid","LLVector3":"Vector3","LLVector3d":"Vector3d","LLVector4":"Vector4","LLQuaternion":"Quaternion","BOOL":"bool","Variable 1":"Vec<u8>","Variable 2":"Vec<u8>","Fixed":"Vec<u8>","IPADDR":"Ipv4Addr","IPPORT":"u16"}
csmap={"U8":"byte","U16":"ushort","U32":"uint","U64":"ulong","S8":"sbyte","S16":"short","S32":"int","S64":"long","F32":"float","F64":"double","LLUUID":"UUID","LLVector3":"Vector3","LLVector3d":"Vector3d","LLVector4":"Vector4","LLQuaternion":"Quaternion","BOOL":"bool","Variable 1":"byte[]","Variable 2":"byte[]","Fixed":"byte[]","IPADDR":"IPAddress","IPPORT":"ushort"}
def gen(lang, mp, comment, classfmt, fieldfmt):
    out=[f"# {lang} Message Stubs (generated from secondlife/master-message-template)\n",
    f"One stub per UDP message ({len(msgs)} messages) in {lang}, generated from message_template.msg field definitions. These are starting points for a codec: implement ToBytes/FromBytes following the field order exactly, honour the zerocoded flag, and verify against LibreMetaverse.Protocol and the viewer template copy before shipping.\n"]
    for mm in msgs:
        out.append(f"\n## {mm['name']} ({mm['freq']} {mm['num']}, {mm['trust']}, {mm['enc']})\n")
        out.append("```"+comment+"\n")
        out.append(classfmt.format(name=mm["name"])+"\n")
        for b in mm["blocks"]:
            rep = "[]" if b["kind"]!="Single" else ""
            out.append(f"  // block {b['name']} ({b['kind']}{' '+b['count'] if b['count'] else ''})\n")
            for fn,ft in b["fields"]:
                out.append(fieldfmt.format(type=mp.get(ft,ft), name=fn, rep=rep)+"\n")
        out.append("}\n```\n")
    return "\n".join(out)
total=0
total+=w("secondlife_protocol","message-stubs-typescript.md", gen("TypeScript", tsmap, "ts", "export interface {name}Message {{", "  {name}: {type}{rep};"))
total+=w("secondlife_protocol","message-stubs-kotlin.md", gen("Kotlin", ktmap, "kotlin", "data class {name}Message(", "  val {name}: {type}, // {rep}"))
total+=w("secondlife_protocol","message-stubs-rust.md", gen("Rust", rsmap, "rust", "pub struct {name}Message {{", "  pub {name}: {type}, // {rep}"))
total+=w("secondlife_protocol","message-stubs-csharp.md", gen("C#", csmap, "csharp", "public sealed class {name}Packet : Packet {{", "  public {type} {name}; // {rep}"))
print("TOTAL6", total)
