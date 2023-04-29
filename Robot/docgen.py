import glob
from importlib.machinery import SourceFileLoader
import inspect

all_files = [x.replace("\\", "/") for x in glob.glob("pibot/**/*.py", recursive=True)]

CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

classes = {}
class_paths = {}

for filename in all_files:
    try:
        mdl = SourceFileLoader("", filename).load_module()

        attrs = dir(mdl)
        for a in attrs:
            if a:
                if a[0] in CAPS:
                    if a not in classes:
                        classes[a] = getattr(mdl, a)
                        class_paths[a] = "pibot" + (
                            inspect.getfile(classes[a])
                            .replace("\\", "/")
                            .split("pibot")[-1]
                            .replace("/", ".")
                            .replace(".py", f".{a}")
                        )

    except ModuleNotFoundError:
        pass


def doc_to_md(doc, level="##"):
    out = ""
    for line in doc.split("\n"):
        if line.strip().startswith("-"):
            last_line = out.split("\n")[-2]
            out = "\n".join(out.split("\n")[:-2])
            out += f"\n\n{level} {last_line}\n\n"
        else:
            if ":" in line or "(" in line:
                out += f"- `{line.strip()}`\\\n"
            elif line:
                out += f"{line.strip()}\n"
    return out


for c in classes:
    dcstr = ""
    full = classes[c]
    attrs = dir(full)

    if full.__doc__ is not None:
        dcstr += f"# {c}\n\n`{class_paths[c]}`\n\n"
        dcstr += doc_to_md(full.__doc__)

        for at in attrs:
            if getattr(full, at).__doc__ is not None:
                if (not at.startswith("_")) or ("__init__" in at):
                    escaped = at.replace("_", "\\_")
                    dcstr += f"## {escaped}\n\n"
                    dcstr += doc_to_md(getattr(full, at).__doc__, "")

        with open(f"docs/{c}.md", "w") as fp:
            fp.write(dcstr[:-1])
