# OPTION 1:
# Import module for downloading SINGLE VIDEO
from pytube import YouTube

# Provide link of video or playlist
vd = YouTube('https://www.youtube.com/watch?v=vEQ8CXFWLZU&ab_channel=InternetMadeCoder')

# Print title and amount of views of video(s)
print("Title: ", vd.title)
print("Views: ", vd.views)

# Download video(s)
vd.streams.get_highest_resolution().download()
print("Video downloaded!")


# OPTION 2:
# Import module for downloading ENTIRE PLAYLIST
from pytube import YouTube
from pytube import Playlist

pl = Playlist("https://www.youtube.com/playlist?list=PL830tyaBUx1quULtBuDo9qOrnz8TYtB4w").video_urls

for video in pl:
    vid = YouTube(video)

    print("Title: ", vid.title)
    print("Views: ", vid.views)

    vid.streams.get_highest_resolution().download()
    print("All videos from playlist downloaded!")
