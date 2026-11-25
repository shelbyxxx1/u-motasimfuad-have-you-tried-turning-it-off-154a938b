import os
from pathlib import Path


LINE = "Good news: I recovered the email where we promised not to lose your files."


def main() -> None:
    assert 1 <= len(LINE) <= 200
    assert "\n" not in LINE and "\r" not in LINE
    output_directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_directory.mkdir(parents=True, exist_ok=True)
    (output_directory / "entry.txt").write_bytes((LINE + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
