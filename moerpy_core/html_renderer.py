from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(
    '/home/skohler/development/playground/moerpy/templates'))

template = env.get_template('movie_list.html')

print template.render(movie='AVATAR (2011)')
