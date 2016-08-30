try:
    import json
    from argparse import Namespace
    import requests
    from urllib import urlencode
except ImportError:
    import json
    from argparse import Namespace
    import requests
    from urllib.parse import urlencode

class YoutubeManager:
    def __init__(self):
        self.author = "ahmetkotan"
        self.author_website = "http://ahmetkotan.com.tr"
        self.api_key = None

        self.APIs = {
            'videos': 'https://www.googleapis.com/youtube/v3/videos',
            'search': 'https://www.googleapis.com/youtube/v3/search',
            'channels': 'https://www.googleapis.com/youtube/v3/channels',
            'playlists': 'https://www.googleapis.com/youtube/v3/playlists',
            'playlistItems':
                'https://www.googleapis.com/youtube/v3/playlistItems'
        }

    def set_api_key(self, api_key):
        self.api_key = api_key
        return True

    def get_api_key(self):
        return self.api_key

    def get_api(self, apiname):
        return self.APIs[apiname]

    def json_to_object(self, json_data):
        x = json.loads(json_data, object_hook=lambda d: Namespace(**d))
        return x

    def api_request(self, url, parameters):
        parameters['key'] = self.api_key

        req_url = url + '?' + urlencode(parameters)

        con = requests.get(req_url)
        data = con.text

        youtube_object = self.json_to_object(data)
        return youtube_object
