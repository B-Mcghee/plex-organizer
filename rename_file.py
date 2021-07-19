import os
import re
from env import HOME, MOVIES, SHOWS, PLEX
from patterns import PATTERN
# path = os.path.split(env_path)
# print(path)
# abs_path = path[0]
# print(abs_path)
# file = path[1]
# title = re_title.search(file).group()
# episode = re_epidose.search(file).group()


# title = title.split('.')
# #count = len(new_title)
# title = ' '.join(title)

# completed_file = title + episode + ext
# print(title, episode, file)
# print(completed_file)
# completed_file = os.path.join(abs_path, completed_file)
# print(completed_file)

#FILES = os.path.isabs(ENV_PATH)


#os.rename(env_path, completed_file)
# length = len(path)
# files = os.listdir(path)
# print(files)
# print(path[0:length+1])
# for file in files:
# Ink.Master.S10E15.720p.HEVC.x265-MeGusta [TD].torrent
#     title = file_title.search(file)
#     series = season.search(file)
#     new_title = str(title.group()).split('.')
#     directory = new_title[0] + ' ' + new_title[1]
#     print(f'{directory} {series.group()}')
#     os.mkdir(path + '/' + directory)
# print(file.group(1))
# print(file.group(2))
re_movie_year = re.compile(r'\d{4}')
re_resolution = re.compile(r'\d{3,4}p')
re_title = re.compile('(\D*)(?![^S])|(\D*)(?![^S])?')
pattern = re.compile(PATTERN)
file_name = 'Teen Wolf S05E17 Webdl [UplaoderKing].mkv'


def convert_spaces(original):
    result = re.sub(' ', '.', original)
    original = os.path.join(SHOWS, original)
    if os.path.basename(original)[0] == '.':
        return
    result = os.path.join(SHOWS, result)
    os.rename(original, result)


def list_directories(path):
    return os.listdir(path)


files = list_directories(SHOWS)
for file in files:
    convert_spaces(file)
# def sub(group):
#     return re.sub('\.', ' ', group)


# def rename_movie(file):

#     movie_title = re_title.search(file)
#     resolution = re_resolution.search(file)
#     movie_year = re_movie_year.search(file)
#     if movie_title and resolution and movie_year:
#         movie_title = sub(movie_title.group())

#     ext = os.path.splitext(file)[1]
#     return f'{movie_title} ({movie_year.group()}) - {resolution.group()}'


# name = rename_movie(file_name)
# print(name)
