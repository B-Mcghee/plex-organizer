

from pathlib import Path
from time import ctime
import re
import os
import shutil
from env import HOME, MOVIES, SHOWS, PLEX
from rename_file import pattern
underscore = re.compile(r'([^._a-zA-Z0-9-[]])|^(\D*)[.]', )
movie_regex = re.compile(
    r'([Ss]\d{2}[Ee]\d{2})')
re_movie_year = re.compile(r'\d{4}')
re_resolution = re.compile(r'\d{3,4}p')
re_title = re.compile('(\D*)(?![^S])|(\D*)(?![^S])?')
re_episode = re.compile(r'([Ss]\d{2}[Ee]\d{2})|(\d{3})')
re_season = re.compile('^([Ss]\d{2})|(\d{3})')
all_files = re.compile(r'^(\D*)\.([Ss]\d{2}[Ee]\d{2})')
with_ex = re.compile(r'(\.\D*)$')


class Folder_Structure:
    def __init__(self) -> None:
        self.

    def list_directories(self, path):
        return os.listdir(path)

    def sub(self, group):
        return re.sub('\.', '', group)

    def movie_folder(title, year, file_name):

        folder = f'{title}({year})'
        path = os.path.join(PLEX, '_Movies')
        if not os.path.isdir(path):
            os.mkdir(path)
        folder = os.path.join(path, folder)
        if not os.path.isdir(folder):
            os.mkdir(folder)
        current_path = os.path.join(MOVIES, file_name)
        shutil.move(current_path, folder)

    def tv_folder(self, title, episode, file_name):
        folder = title + episode
        season = re_season.search(episode)
        if season.group(1):
            season = season.group(1)
        else:
            season = 'S0' + season.group(2)[0]
        path = os.path.join(PLEX, '_TV Shows')
        if not os.path.isdir(path):
            os.mkdir(path)
        folder = os.path.join(path, title)
        if not os.path.isdir(folder):
            os.mkdir(folder)
        season = os.path.join(folder, season)
        if not os.path.isdir(season):
            os.mkdir(season)
        current_path = os.path.join(SHOWS, file_name)
        shutil.move(current_path, season)

        # completed_file = os.path.join(abs_path, completed_file)
    # print(completed_file)

    def separate_file_structure(self, folder):
        if folder == 'Movies':
            files = self.list_directories(MOVIES)
            for file in files:
                item = pattern.search(file)
                if item:
                    title = item.group('title')
                    year = item.group('year')
                    # movie_title = re_title.search(item.group('title'))
                    # # resolution = re_resolution.search(item)
                    # movie_year = re_movie_year.search(item.group('year'))
                    # if movie_title and movie_year:
                    #movie_title = sub(movie_title.group())
                    self.movie_folder(title, year, file)
        if folder == 'Shows':
            files = self.list_directories(SHOWS)
            # print(files)
            for file in files:
                item = pattern.search(file)
                if item:
                    title = item.group('title')
                    episode = re_episode.search(title).group()
                    title = re_title.search(item.group())

                    if title and episode:

                        # ext = ' '  # os.path.splitext(item.group())[1]
                        self.tv_folder(title.group(), episode, file)

    files = list_directories(HOME)
    for file in files:
        separate_file_structure(file)
