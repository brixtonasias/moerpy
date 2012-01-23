from nose.tools import *
from moerpy_core.data import Movie


def test_create_movie():
    movie_title_src = "Avatar (2011)"
    movie_title_target = "Avatar Official Trailer"
    movie_url = "http://yt.com/test-file"
    m = Movie(movie_title_src, movie_title_target, movie_url)
    assert_equal(m.title_in_source, movie_title_src)
    assert_equal(m.title_in_platform, movie_title_target)
    assert_equal(m.url, movie_url)
