import os
import sys
from pathlib import Path

if (len(sys.argv) == 3):
    extension = sys.argv[1]
    pattern = sys.argv[2]

    entries = Path('')

    entries_to_change = []

    for i in entries.iterdir():
        if str(i).endswith(f".{extension}"):
            print(f"{i} appended")
            entries_to_change.append(i)

    for i in range(len(entries_to_change)):
        os.system(f"mv {entries_to_change[i]} {pattern}{i}.{extension}")

else:
    print("Usage: python3 index.py <file-extension> <pattern-to-name>")
