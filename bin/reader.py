import os
import gdata.youtube
import gdata.youtube.service
from sys import argv

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
    for file_or_folder in listing:
        if not file_or_folder.startswith('.'):
            print "Current file is: " + file_or_folder
            query.vq = file_or_folder + ', movie, trailer, official'
            feed = yt_service.YouTubeQuery(query)
            movie_name = find_movie_title(file_or_folder)
            return_list = []
            for entry in feed.entry:
                if entry.media.duration.seconds > 60:
                    if movie_name in entry.media.title.text:
                        # TODO: Create movie object and add to
                        # TODO: return_list
                        print entry.media.title.text
                        print entry.GetSwfUrl()
                        print entry.media.thumbnail[0].url
                        print entry.media.player.url
                        break
            return return_list


find_movies_in_folder(listing)
