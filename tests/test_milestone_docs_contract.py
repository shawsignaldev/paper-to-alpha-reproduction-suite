from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_milestone_depth_docs_exist() -> None:
    for relative in [
        "docs/system-design.md",
        "docs/validation-evidence.md",
        "docs/operating-boundaries.md",
    ]:
        path = ROOT / relative
        assert path.exists(), f"missing {relative}"
        text = path.read_text(encoding="utf-8")
        assert len(text.split()) >= 130
        assert "##" in text

def test_readme_links_milestone_depth_docs() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for relative in [
        "docs/system-design.md",
        "docs/validation-evidence.md",
        "docs/operating-boundaries.md",
    ]:
        assert relative in readme
