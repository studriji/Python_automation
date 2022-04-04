#python -m pip install --upgrade pytube
#pip install pytube3

import re
from pytube import *
url = 'https://www.youtube.com/playlist?list=PL-ZbNfIz7zVG2Qs-piBJy6BOBpZgmET8g'
playlist = Playlist(url)
#print(playlist._video_regex)
#print(playlist)

try:
    playlist._video_regex = re.compile(r'\"url\":\"(/watch\?v=[\w-]*)') # we created a object here, not a variable
    print(playlist._video_regex)
    print(type(playlist))
    for video in playlist.videos:
        print(video)
        #video.streams.get_highest_resolution().download('download')
       
except Exception as e:
    print(e)
print('download complete')

#actually the html page is loaded and then a regex search takes place for the pattern like /watch/v=?
# the regex expression used was href=\"url\":\"(/watch\?v=[\w-]*)

#re : regular exoression : used to check if a string has the specified search pattern
#re.compile is used to compile a regular expression pattern provided as a string into a regex pattern object
#later this object can be used to search for a match inside different target strings