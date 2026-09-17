from pathlib import Path

ROOT = Path(".")

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "node_modules",
    ".idea",
    ".vscode",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
}

IGNORE_FILES = {
    ".DS_Store",
}

output_file = ROOT / "project_structure.txt"

with output_file.open("w", encoding="utf-8") as f:
    for path in sorted(ROOT.rglob("*")):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.name in IGNORE_FILES:
            continue

        f.write(str(path.relative_to(ROOT)) + "\n")

print(f"Project structure saved to: {output_file.resolve()}")