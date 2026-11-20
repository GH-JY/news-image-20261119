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

# The repository root is the directory that holds this program, and the
# entry image sits at its root; resolving it here keeps the program working
# whatever directory it is started from.
REPO_DIR = Path(__file__).resolve().parent
SOURCE_IMAGE = REPO_DIR / "entry.png"


def main() -> None:
    # The grader sets no variable and reads /output; outside it, the
    # variable names a directory, created here if it does not exist yet.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    # A byte-for-byte copy is deterministic: both grader runs produce the
    # same file, as the rules require.
    shutil.copyfile(SOURCE_IMAGE, output_dir / "entry.png")


if __name__ == "__main__":
    main()
