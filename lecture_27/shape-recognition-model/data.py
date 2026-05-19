"""
DataManager — loads 8×8 bitmap training samples from a directory tree.

Expected layout:
    <data_dir>/
        triangle/   01.txt  02.txt  ...
        circle/     01.txt  ...
        square/     01.txt  ...

Each .txt file is one sample: 8 lines of 8 characters, '*' = filled, '.' = empty.
The label is derived from the subdirectory name.

Bitmap encoding
    1.0  →  filled pixel  ('*')
    0.0  →  empty pixel   ('.')

Label encoding (matches LABELS index)
    0  →  triangle
    1  →  circle
    2  →  square
"""

import os


class DataManager:
    GRID   = 8
    LABELS = ["triangle", "circle", "square", "trash"]

    # ── Public API ────────────────────────────────────────────────────────────

    def get_training_data(self, data_dir: str) -> list:
        """
        Load all bitmap files from data_dir and return (bitmap, label) pairs.
        Files are read from <data_dir>/<label_name>/*.txt.
        Prints a summary of all loaded samples.
        """
        data = []
        for label_idx, name in enumerate(self.LABELS):
            class_dir = os.path.join(data_dir, name)
            if not os.path.isdir(class_dir):
                continue
            for fname in sorted(f for f in os.listdir(class_dir) if f.endswith(".txt")):
                bitmap = self.load_bitmap(os.path.join(class_dir, fname))
                data.append((bitmap, label_idx))

        self._print_dataset(data)
        return data

    @classmethod
    def load_bitmap(cls, filepath: str) -> list:
        """Read a bitmap .txt file and return a flat list of 64 floats."""
        pixels = []
        with open(filepath) as f:
            for line in f:
                for ch in line.rstrip("\n"):
                    if ch == "*":
                        pixels.append(1.0)
                    elif ch == ".":
                        pixels.append(0.0)
        pixels = pixels[: cls.GRID * cls.GRID]
        while len(pixels) < cls.GRID * cls.GRID:
            pixels.append(0.0)
        return pixels

    # ── Logging ───────────────────────────────────────────────────────────────

    @classmethod
    def _print_dataset(cls, data: list) -> None:
        print("Loaded training data:\n")
        for label_idx, name in enumerate(cls.LABELS):
            bitmaps = [b for b, l in data if l == label_idx]
            print(f"  {name}s ({len(bitmaps)} samples)")
            cls._print_bitmaps_side_by_side(bitmaps)

    @classmethod
    def _print_bitmaps_side_by_side(cls, bitmaps: list, per_row: int = 4) -> None:
        gap = "   "
        for start in range(0, len(bitmaps), per_row):
            chunk = bitmaps[start : start + per_row]
            header = gap.join(f"#{start + i + 1:<{cls.GRID}}" for i in range(len(chunk)))
            print("    " + header)
            for row in range(cls.GRID):
                cells = [
                    "".join("*" if b[row * cls.GRID + c] else "." for c in range(cls.GRID))
                    for b in chunk
                ]
                print("    " + gap.join(cells))
            print()

    # ── Utility ───────────────────────────────────────────────────────────────

    @staticmethod
    def render(bitmap: list, cols: int = 8) -> str:
        """Convert a flat bitmap list back to a printable grid string."""
        rows = []
        for r in range(len(bitmap) // cols):
            row = "".join("*" if bitmap[r * cols + c] else "." for c in range(cols))
            rows.append(row)
        return "\n".join(rows)
