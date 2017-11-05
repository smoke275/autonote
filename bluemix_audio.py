# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:19:20 2017

@author: shash
"""

from pytube import YouTube
from pydub import AudioSegment

yt = YouTube('https://www.youtube.com/watch?v=mbyG85GZ0PI')
'''
yt.streams.filter(progressive=True).filter(file_extension='mp4')\
.order_by('resolution').desc().first().download()
#yt.streams.filter(progressive=True).filter(file_extension='mp4').filter(only_video=True).desc().first().download()
print(yt.title+'.mp4')
'''
mp4_version = AudioSegment.from_file(yt.title+'.mp4', "mp4")
mp4_version = mp4_version[1000:500000]
mp4_version.export(yt.title+'.mp3', format="mp3")
print('Done')


import requests
head = {'Content-Type':'audio/mpeg',\
        'Transfer-Encoding':'chunked',\
        }
url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
data = open(yt.title+'.mp3', 'rb').read()
ret = requests.post(url, data = data, \
                    auth=('d18ba3bd-41d3-46ed-b72f-994b234e3c4a','cibwiPkwnPMt'))
print(ret.status_code)
print(ret.json())