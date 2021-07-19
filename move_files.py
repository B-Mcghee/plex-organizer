
from pathlib import Path
from time import ctime
import os
import shutil
from env import PLEX, HOME

file_name = 'Taken.2.2012.UNRATED.EXTENDED.1080p.BRRip.x264.AAC-m2g.mkv'


def movie_into_folder(path, file, title):
    '''
        check if directory exists
        get directory name
        compare directory name to file name lower case
        if match move file in movie folder
    '''
    # check if directory exists
    created_path = os.path.join(path, title)
