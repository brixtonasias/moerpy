import os
from sys import argv

script_name, folder_to_search = argv

print folder_to_search

path = '/Volumes/Multimedia/'
listing = os.listdir(folder_to_search)

for infile in listing:
    if not infile.startswith('.'):
        # TODO Call youtube API here to get info on trailers
        # TODO then hand this over to parsing the/a template
        print "Current file is: " + infile
