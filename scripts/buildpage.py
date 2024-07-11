import sys
from pathlib import Path
from string import Template


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
    if page_name == "index":
        return ""

    return page_name.title().replace("-", " ") + " | "


def build(page_file: Path) -> None:
    public_dir = Path("public")

    base_file = load_base(Path("base.html"))

    content = page_file.read_text()

    title = pagetitle(page_file.stem)

    # 'full' html pages don't need the base template
    if content.startswith("<!DOCTYPE html>"):
        output = content
    else:
        output = base_file.substitute(content=content, subtitle=title)

    target_file = public_dir / page_file.name
    target_file.write_text(output)

    print(f"{str(page_file)} => {target_file}")


if __name__ == "__main__":
    pages = [Path(page) for page in sys.argv[1:] or Path("pages").iterdir()]

    for page in pages:
        build(page)
