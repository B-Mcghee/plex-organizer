
from pathlib import Path
from time import ctime
import re
import os
import shutil

movie_regex = re.compile(
    r'([Ss]\d{2}[Ee]\d{2})')
all_files = re.compile(r'(\D*)\.([Ss]\d{2}[Ee]\d{2})')
with_ex = re.compile(r'(\.\D*)$')
path = Path('/Volumes/THE DRIVE/testing/')
# paths = [p for p in path.rglob('*.torrent') if movie_regex.search(str(p))]

paths = [p for p in path.rglob('*.*')]
# print(paths)
for p in paths:
    file = all_files.search(str(p))
    extension = with_ex.search(str(p))
    print(str(p))
    if file:
        print(file.group(1))
        print(file.group(2))
    folder = Path('/Volumes/THE DRIVE/testing/folder')
    if Path(str(p)).is_file() or Path(str(p)).is_dir():
        shutil.move(str(p), folder)
