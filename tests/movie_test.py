from nose.tools import *
from moerpy_core.data import Movie


def test_create_movie():
    file_name = "Avatar (2011) extended"
    movie_title_src = "Avatar (2011)"
    movie_title_target = "Avatar Official Trailer"
    swf_url = "http://yt.com/swf_url"
    player_url = "http://yt.com/player_url"
    m = Movie(file_name,
            movie_title_src,
            movie_title_target,
            swf_url,
            player_url)
    assert_equal(m.title_in_source, movie_title_src)
    assert_equal(m.title_in_platform, movie_title_target)
    assert_equal(m.swf_url, swf_url)
    assert_equal(m.file_name, file_name)
    assert_equal(m.player_url, player_url)
