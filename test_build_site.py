from build_site import TEMPLATE, build, demo_rows, render
from version import __version__


def test_render_puts_version_in_page():
    page = render("<p>v{{VERSION}}</p>", "2.3.4", [])
    assert page == "<p>v2.3.4</p>"


def test_render_adds_demo_rows():
    page = render("{{DEMO_ROWS}}", "1.0.0", [("average([1, 2])", 1.5)])
    assert "<code>average([1, 2])</code>" in page
    assert "<code>1.5</code>" in page


def test_render_escapes_html():
    page = render("{{DEMO_ROWS}}", "1.0.0", [("<b>", "<script>")])
    assert "<script>" not in page
    assert "&lt;b&gt;" in page


def test_demo_rows_use_cleaner_results():
    results = [result for _, result in demo_rows()]
    assert results == ["Alice Smith", [3, 1, 2], 90]


def test_template_has_placeholders():
    template = TEMPLATE.read_text(encoding="utf-8")
    assert "{{VERSION}}" in template
    assert "{{DEMO_ROWS}}" in template


def test_build_writes_page_with_current_version(tmp_path):
    output_path = build(output_dir=tmp_path)
    page = output_path.read_text(encoding="utf-8")
    assert output_path == tmp_path / "index.html"
    assert f"version {__version__}" in page
    assert "{{" not in page
