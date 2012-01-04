import os

path = '/Volumes/Multimedia/'
listing = os.listdir(path)

for infile in listing:
    if not infile.startswith('.'):
        print "Current file is: " + infile
