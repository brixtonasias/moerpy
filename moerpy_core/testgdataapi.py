import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()
query = gdata.youtube.service.YouTubeVideoQuery()
query.vq = 'avatar, movie, trailer, official'
query.orderby = 'viewCount'
query.racy = 'include'
feed = yt_service.YouTubeQuery(query)

for entry in feed.entry:
    if entry.media.duration.seconds > 60:
        if "Avatar" in entry.media.title.text:
            print entry.media.title.text
            print entry.GetSwfUrl()
