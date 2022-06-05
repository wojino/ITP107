import re
import sys
import os.path

tvshows = {}
ratings = {}

def input_filename():
    filename = input('Enter the filename: ')

    if not filename or not os.path.isfile(filename):
        print('Invalid filename')
        sys.exit(1)

    return filename

def parse_tvshow(line):
    line = line.strip().lower()
    p = re.compile(r'(the )?(a )?\s*(?P<title>[^-.]+?)\s*[-.]\s*((s(?P<season>\d+))?(((e(?P<episode_start>\d+))(?:-e?(?P<episode_end>\d+))?)?))?\s*,\s*(?P<rating>.+)')
    m = re.fullmatch(p, line)
    if m:
        title = m.group('title')
        if m.group('season'):
            season = int(m.group('season'))
        else:
            season = 1
        if m.group('episode_start'):
            episode_start = int(m.group('episode_start'))
        else:
            episode_start = 1
        if m.group('episode_end'):
            episode_end = int(m.group('episode_end'))
        else:
            episode_end = episode_start
        rating = float(m.group('rating'))

        return (title, season, episode_start, episode_end, rating)

    else:
        return False

def dictionary_tvshows(tvshow_info):
    title, season, episode_start, episode_end, rating = tvshow_info
    if title not in tvshows:
        tvshows[title] = []
    
    for i in range(episode_start, episode_end + 1):
        tvshows[title].append([season, i, rating])

def rating_tvshows(tvshow_info):
    title, season, episode_start, episode_end, rating = tvshow_info
    if title not in ratings:
        ratings[title] = []
    
    for i in range(episode_start, episode_end + 1):
        ratings[title].append(rating)

def input_tvshows(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        if not parse_tvshow(line):
            print(f'Could not be parsed: {line}')
            continue
        else:
            tvshow_info = parse_tvshow(line)
            dictionary_tvshows(tvshow_info)
            rating_tvshows(tvshow_info)

    f.close()

def print_tvshows(tvshows):
    for title, value in tvshows.items():
        print(title)
        print('=' * len(title))
        print(f'Average rating: {sum(ratings[title]) / len(ratings[title]):.3f}')
        print('    Season   Episode    Rating')
        for season, episode, rating in value:
            print(f'        {season:>02}        {episode:>02}{rating:>10.2f}')
        print('\n')

if __name__ == '__main__':
    filename = input_filename()
    input_tvshows(filename)
    print_tvshows(tvshows)
