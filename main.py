# SPDX-License-Identifier: MIT
# The Poster for a Place That Isn't There — make.fun bounty
# the-poster-for-a-place-that-i-2-20261121-0539
# Writes the travel poster for VELMARIS, the Floating Harbour,
# to /output/entry.png. No network, no randomness: every run
# writes the same bytes.

from pathlib import Path

# The poster image, stored beside this program as poster.jpg
# (896 x 896 JPEG, 109,110 bytes).
POSTER_PATH = Path(__file__).resolve().parent / "poster.jpg"

OUT_PATH = Path("/output/entry.png")


def main() -> None:
    data = POSTER_PATH.read_bytes()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_bytes(data)


if __name__ == "__main__":
    main()
