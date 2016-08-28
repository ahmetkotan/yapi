#-*- coding:utf-8 -*-


from manager import YoutubeManager

manager = YoutubeManager()
author = "ahmetkotan"
author_website = "http://ahmetkotan.com.tr"

class YoutubeAPI():
    def __init__(self, api_key):
        manager.setAPIKey(api_key)

    def getApiKey(self):
        return manager.getAPIKey()

    def changeApiKey(self, api_key):
        manager.setAPIKey(api_key)

    def getVideoInfo(self, video_id):
        api_url = manager.getAPI('videos')
        params = {
            'id': video_id,
            'key': self.getApiKey(),
            'part': 'id, snippet, contentDetails, player, statistics, status'
        }

        video = manager.apiRequest(api_url, params)
        return video

    def generalSearch(self, keyword, max_results=10):
        api_url = manager.getAPI('search')
        params = {
            'q': keyword,
            'part': 'id, snippet',
            'maxResults': max_results
        }

        objects = manager.apiRequest(api_url, params)
        return objects

    def videoSearch(self, keyword, max_results=10):
        api_url = manager.getAPI('search')
        params = {
            'q': keyword,
            'type': 'video',
            'part': 'id, snippet',
            'maxResults': max_results
        }

        videos = manager.apiRequest(api_url, params)
        return videos

    def videoSearchInChannel(self, keyword, channel_id, max_results=10):
        api_url = manager.getAPI('search')
        params = {
            'q': keyword,
            'type': 'video',
            'channelId': channel_id,
            'part': 'id, snippet',
            'maxResults': max_results
        }

        videos = manager.apiRequest(api_url, params)


    def getChannelByName(self, channel_name):
        api_url = manager.getAPI('channels')
        params = {
            'forUsername': channel_name,
            'part': 'id,snippet,contentDetails,statistics,invideoPromotion'
        }

        channel = manager.apiRequest(api_url, params)
        return channel

    def getChannelById(self, channel_id):
        api_url = manager.getAPI('channels')
        params = {
            'id': channel_id,
            'part': 'id,snippet,contentDetails,statistics,invideoPromotion'
        }

        channel = manager.apiRequest(api_url, params)
        return channel

    def getPlaylistById(self, playlist_id):
        api_url = manager.getAPI('playlist')
        params = {
            'id': playlist_id,
            'part': 'id, snippet, status'
        }

        playlist = manager.apiRequest(api_url, params)
        return playlist

    def getPlaylistByChannelId(self, channel_id):
        api_url = manager.getAPI('playlist')
        params = {
            'channelId': channel_id,
            'part': 'id, snippet, status'
        }

        playlist = manager.apiRequest(api_url, params)
        return playlist

    def getPlaylistItemsByPlaylistId(self, playlist_id, max_results=50):
        api_url = manager.getAPI('playlistItems')
        params = {
            'playlistId': playlist_id,
            'part': 'id, snippet, contentDetails, status',
            'maxResults': max_results
        }

        playlist_items = manager.apiRequest(api_url, params)
        return playlist_items



