import os
import sys
from pathlib import Path
from string import Template
import shutil


def clean_dir(directory: Path) -> None:
    directory.mkdir(exist_ok=True)

    if directory.is_absolute():
        sys.exit(f"ERROR: dangerous path '{directory}'. Not removing.")

    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            Path(root, name).unlink()
        for name in dirs:
            Path(root, name).rmdir()


def load_base(filename: Path) -> Template:
    if not filename.exists():
        sys.exit(f"ERROR: base file '{filename}' does not exit")

    with open(filename, "r") as f:
        base = f.read()

    template = Template(base)
    if not template.is_valid():
        sys.exit(
            "ERROR: template is not valid. Check for dollar signs."
            + "\nsee https://docs.python.org/3/library/string.html#template-strings"
        )
    return Template(base)


def pagetitle(page_name: str) -> str:
    if page_name != "index":
        return page_name.title().replace("-", " ") + " | "

    return ""


def build_site(working_dir: str) -> None:
    cwd = Path(working_dir)
    public_dir = cwd / "public"
    static_dir = cwd / "static"
    pages_dir = cwd / "pages"

    print(f"starting build in {public_dir.absolute()}...")

    clean_dir(public_dir)

    # move all static files
    for child in static_dir.iterdir():
        target = public_dir / child.name
        if child.is_dir():
            shutil.copytree(child, target)
        else:
            shutil.copy(child, target)

        print(f"{str(child): <25} => {target}")

    # load base template
    base_file = load_base(cwd / "base.html")

    # build pages from base + page and write to public
    for page_file in Path(pages_dir).iterdir():
        content = page_file.read_text()

        title = pagetitle(page_file.stem)

        output = base_file.substitute(content=content, subtitle=title)

        target_file = public_dir / page_file.name
        target_file.write_text(output)

        print(f"{str(page_file): <25} => {target_file}")


if __name__ == "__main__":
    build_site(".")
