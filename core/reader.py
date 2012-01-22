import os
from sys import argv
import gdata.youtube
import gdata.youtube.service

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


for infile in listing:
    if not infile.startswith('.'):
        # TODO Call youtube API here to get info on trailers
        # TODO then hand this over to parsing the/a template
        print "Current file is: " + infile
        query.vq = infile + ', movie, trailer, official'
        feed = yt_service.YouTubeQuery(query)
        movie_name = find_movie_title(infile)

        for entry in feed.entry:
            if entry.media.duration.seconds > 60:
                if movie_name in entry.media.title.text:
                    print entry.media.title.text
                    print entry.GetSwfUrl()
                    break
