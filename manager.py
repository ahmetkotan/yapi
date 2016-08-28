#-*- coding:utf-8 -*-

import json
from argparse import Namespace
import urllib, urllib2

class YoutubeManager():
    def __init__(self):
        self.author = "ahmetkotan"
        self.author_website = "http://ahmetkotan.com.tr"

        self.APIs = {
            'videos': 'https://www.googleapis.com/youtube/v3/videos',
            'search': 'https://www.googleapis.com/youtube/v3/search',
            'channels': 'https://www.googleapis.com/youtube/v3/channels',
            'playlists': 'https://www.googleapis.com/youtube/v3/playlists',
            'playlistItems': 'https://www.googleapis.com/youtube/v3/playlistItems',
        }

    def setAPIKey(self, api_key):
        self.api_key = api_key

    def getAPIKey(self):
        return self.api_key

    def getAPI(self, apiname):
        return self.APIs[apiname]

    def jsonToObject(self, json_data):
        x = json.loads(json_data, object_hook=lambda d: Namespace(**d))
        return x


    def apiRequest(self, url, parameters):
        parameters['key'] = self.api_key

        req_url = url + '?' + urllib.urlencode(parameters)
        req = urllib2.urlopen(req_url)
        data = req.read()
        req.close()

        youtube_object = self.jsonToObject(data)
        return youtube_object



