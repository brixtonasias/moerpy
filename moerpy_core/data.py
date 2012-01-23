class Movie(object):

    def __init__(self, file_name, title_in_source, title_in_platform,
            swf_url, player_url):
        self.file_name = file_name
        self.title_in_source = title_in_source
        self.title_in_platform = title_in_platform
        self.swf_url = swf_url
        self.player_url = player_url
