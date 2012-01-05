import os

movie_titles = ['Avatar (2011)', 'Die Hard 4.0', 'Green Street Elite',
'Titanic', 'The Expendables', 'Hitch', 'I am Legend', 'The Dark Knight']

for title in movie_titles:
    directory = 'movies/%s' % title
    if not os.path.exists(directory):
        os.makedirs(directory)
        print '%s successfully created' % directory
    else:
        print '%s already exists' % directory

