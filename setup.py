try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple project that will create trailer lists',
    'author': 'Stefan Kohler',
    'author_email': 'sk+moerpy@stfnkhlr.de',
    'version': '0.1',
    'install_requires': ['nose', 'gdata', 'jinja2'],
    'packages': ['moerpy'],
    'scripts': [],
    'name': 'moerpy'
}

setup(**config)
