import site
site.addsitedir('../')

import os
import gdata.youtube
import gdata.youtube.service
from sys import argv
from moerpy_core.data import Movie

script_name, folder_to_search = argv

print folder_to_search

yt_service = gdata.youtube.service.YouTubeService()
query = gdata.youtube.service.YouTubeVideoQuery()
query.orderby = 'viewCount'
query.racy = 'include'

listing = os.listdir(folder_to_search)


def find_movie_title(file_or_folder):
    position = file_or_folder.find('(')
    if position > 0:
        print '( found at position %s' % position
        return file_or_folder[:position - 1]
    return file_or_folder


def find_movies_in_folder(listing):
    return_list = []

    for file_or_folder in listing:

        if not file_or_folder.startswith('.'):
            print "Current file is: " + file_or_folder
            query.vq = file_or_folder + ', movie, trailer, official'
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
    return return_list


find_movies_in_folder(listing)
