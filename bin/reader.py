import site
site.addsitedir('../')

import os
import gdata.youtube
import gdata.youtube.service
from sys import argv
from moerpy_core.data import Movie
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(
    '../templates'))
script_name, folder_to_search = argv

yt_service = gdata.youtube.service.YouTubeService()
query = gdata.youtube.service.YouTubeVideoQuery()
query.orderby = 'viewCount'
query.racy = 'include'

file_listing = os.listdir(folder_to_search)


def find_movie_title(file_or_folder):
    position = file_or_folder.find('(')
    if position > 0:
        return file_or_folder[:position - 1]
    return file_or_folder


def find_movies_in_folder(listing):
    return_list = []

    for file_or_folder in listing:

        if not file_or_folder.startswith('.'):
            query.vq = file_or_folder + ', movie, trailer'
            feed = yt_service.YouTubeQuery(query)
            movie_name = find_movie_title(file_or_folder)
            for entry in feed.entry:
                if entry.media.duration.seconds > 60:
                    if movie_name in entry.media.title.text:
                        m = Movie(file_or_folder,
                                movie_name,
                                entry.media.title.text,
                                entry.GetSwfUrl(),
                                entry.media.player.url)
                        return_list.append(m)
                        break
    return return_list

template = env.get_template('movie_list.html')
print template.render(movies=find_movies_in_folder(file_listing))
