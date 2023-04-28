import glob
from importlib.machinery import SourceFileLoader

all_files = [x.replace("\\", "/") for x in glob.glob("pibot/**/*.py", recursive=True)]

CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

classes = {}

for filename in all_files:
    try:
        mdl = SourceFileLoader("", filename).load_module()
        attrs = dir(mdl)
        for a in attrs:
            if a:
                if a[0] in CAPS:
                    if a not in classes:
                        classes[a] = getattr(mdl, a)

    except ModuleNotFoundError:
        pass


for c in classes:
    dcstr = ""
    full = classes[c]
    attrs = dir(full)

    if full.__doc__ is not None:
        dcstr += f"# {c}\n\n"
        for line in full.__doc__.split("\n"):
            if line.strip().startswith("-"):
                last_line = dcstr.split("\n")[-2]
                dcstr = "\n".join(dcstr.split("\n")[:-2])
                dcstr += f"\n\n## {last_line}\n\n"
            else:
                if ":" in line or "(" in line:
                    dcstr += f"- `{line.strip()}`\\\n"
                elif line:
                    dcstr += f"{line.strip()}\n"

        with open(f"docs/{c}.md", "w") as fp:
            fp.write(dcstr[:-1])
