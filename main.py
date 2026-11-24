"""Entry for news-image-20261123: one image of the world news of Monday 23 November 2026.

The image (art.jpg, a newspaper front page naming the date and five stories
from that day) is copied byte for byte to the output directory as entry.png.
No network, no randomness: every run writes identical bytes.
"""

import os
import shutil
from pathlib import Path

SOURCE_NAME = "art.jpg"
OUTPUT_NAME = "entry.png"


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    shutil.copyfile(source, target)
    # Guard against a truncated write: the output must be the whole image.
    if target.stat().st_size != source.stat().st_size:
        raise RuntimeError("entry.png size does not match art.jpg")


if __name__ == "__main__":
    main()
