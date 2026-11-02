"""Build the website: put the version and a demo into site/index.html."""

from html import escape
from pathlib import Path

from cleaner import average, clean_name, remove_duplicates
from version import __version__

PROJECT_DIR = Path(__file__).parent
TEMPLATE = PROJECT_DIR / "site" / "index.html"
OUTPUT_DIR = PROJECT_DIR / "_site"


def demo_rows():
    """Return (code, result) pairs that show the cleaner functions."""
    return [
        ('clean_name("  aLiCe   smith ")', clean_name("  aLiCe   smith ")),
        ("remove_duplicates([3, 1, 3, 2, 1])", remove_duplicates([3, 1, 3, 2, 1])),
        ("average([80, 90, 100])", average([80, 90, 100])),
    ]


def render(template, version, rows):
    """Fill the template with the version and the demo table rows."""
    table = "\n".join(
        f"        <tr><td><code>{escape(code, quote=False)}</code></td>"
        f"<td><code>{escape(repr(result), quote=False)}</code></td></tr>"
        for code, result in rows
    )
    page = template.replace("{{VERSION}}", escape(version))
    return page.replace("{{DEMO_ROWS}}", table)


def build(template_path=TEMPLATE, output_dir=OUTPUT_DIR):
    """Write the finished page to output_dir/index.html and return its path."""
    template = template_path.read_text(encoding="utf-8")
    page = render(template, __version__, demo_rows())
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "index.html"
    output_path.write_text(page, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    print(f"Website built: {build()}")
