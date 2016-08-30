from manager import YoutubeManager

manager = YoutubeManager()
author = "ahmetkotan"
author_website = "http://ahmetkotan.com.tr"


class YoutubeAPI:
    def __init__(self, api_key):
        manager.set_api_key(api_key)

    def get_api_key(self):
        return manager.get_api_key()

    def change_api_key(self, api_key):
        return manager.set_api_key(api_key)

    def get_video_info(self, video_id):
        api_url = manager.get_api('videos')
        params = {
            'id': video_id,
            'part': 'id, snippet, contentDetails, player, statistics, status'
        }

        video = manager.api_request(api_url, params)
        return video

    def general_search(self, keyword, max_results=10):
        api_url = manager.get_api('search')
        params = {
            'q': keyword,
            'part': 'id, snippet',
            'maxResults': max_results
        }

        objects = manager.api_request(api_url, params)
        return objects

    def video_search(self, keyword, max_results=10):
        api_url = manager.get_api('search')
        params = {
            'q': keyword,
            'type': 'video',
            'part': 'id, snippet',
            'maxResults': max_results
        }

        videos = manager.api_request(api_url, params)
        return videos

    def video_search_in_channel(self, keyword, channel_id, max_results=10):
        api_url = manager.get_api('search')
        params = {
            'q': keyword,
            'type': 'video',
            'channelId': channel_id,
            'part': 'id, snippet',
            'maxResults': max_results
        }

        videos = manager.api_request(api_url, params)
        return videos

    def get_channel_by_name(self, channel_name):
        api_url = manager.get_api('channels')
        params = {
            'forUsername': channel_name,
            'part': 'id,snippet,contentDetails,statistics,invideoPromotion'
        }

        channel = manager.api_request(api_url, params)
        return channel

    def get_channel_by_id(self, channel_id):
        api_url = manager.get_api('channels')
        params = {
            'id': channel_id,
            'part': 'id,snippet,contentDetails,statistics,invideoPromotion'
        }

        channel = manager.api_request(api_url, params)
        return channel

    def get_playlist_by_id(self, playlist_id):
        api_url = manager.get_api('playlist')
        params = {
            'id': playlist_id,
            'part': 'id, snippet, status'
        }

        playlist = manager.api_request(api_url, params)
        return playlist

    def get_playlist_by_channel_id(self, channel_id):
        api_url = manager.get_api('playlist')
        params = {
            'channelId': channel_id,
            'part': 'id, snippet, status'
        }

        playlist = manager.api_request(api_url, params)
        return playlist

    def get_playlist_items_by_playlist_id(self, playlist_id, max_results=50):
        api_url = manager.get_api('playlistItems')
        params = {
            'playlistId': playlist_id,
            'part': 'id, snippet, contentDetails, status',
            'maxResults': max_results
        }

        playlist_items = manager.api_request(api_url, params)
        return playlist_items
