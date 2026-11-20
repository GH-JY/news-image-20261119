"""Copy the entry image to the output directory.

The grader runs this program in a fresh container with no network, the
repository mounted read-only at /bot and a writable /output. Outside the
grader, the environment variable MAKEFUN_OUTPUT_DIR stands in for /output.

The image itself is the finished deliverable: entry.png beside this file.
The program only copies its bytes, so two runs write identical files.
"""

import os
import shutil
from pathlib import Path
from typing import NoReturn

# The repository root is the directory that holds this program, and the
# entry image sits at its root; resolving it here keeps the program working
# whatever directory it is started from.
REPO_DIR = Path(__file__).resolve().parent
SOURCE_IMAGE = REPO_DIR / "entry.png"


def fail(message: str) -> NoReturn:
    """Report a problem on standard error and exit non-zero.

    SystemExit with a string prints it to stderr and exits with status 1,
    so nothing is written to the output directory when this is reached.
    """
    raise SystemExit(f"error: {message}")


def check_source_image() -> None:
    """Refuse to run unless the entry image is a readable regular file.

    This runs before the output directory is created, so a broken source
    leaves no half-made output behind.
    """
    if not SOURCE_IMAGE.is_file():
        fail(f"entry image is missing or not a regular file: {SOURCE_IMAGE}")

    # is_file() says it exists; opening it proves it can actually be read.
    try:
        with SOURCE_IMAGE.open("rb"):
            pass
    except OSError as exc:
        fail(f"entry image cannot be read: {SOURCE_IMAGE}: {exc}")


def main() -> None:
    check_source_image()

    # The grader sets no variable and reads /output; outside it, the
    # variable names a directory, created here now the source is known good.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    # A byte-for-byte copy is deterministic: both grader runs produce the
    # same file, as the rules require.
    shutil.copyfile(SOURCE_IMAGE, output_dir / "entry.png")


if __name__ == "__main__":
    main()
