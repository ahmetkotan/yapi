yapi
===================
#### Python - Youtube Data API v3

**yapi** is a simple client api for youtube.It uses [Youtube Data API v3](https://developers.google.com/youtube/v3/).Before you can use, you must a create project in [here](https://console.developers.google.com/apis/api/youtube/overview).

## Installation
``` 
sudo pip install yapi
```

## Using
```python
import yapi
api = yapi.YoutubeAPI('api_key')
```

## References
```python
video = api.get_video_info('video_id')

results = api.general_search('keyword', max_results=10)
videos = api.video_search('keyword', max_results=10, order=None)
videos = api.video_search_in_channel('keyword', 'channel_id', max_results=10, order=None)

channel = api.get_channel_by_name('channel_name')
channel = api.get_channel_by_id('channel_id')

playlist = api.get_playlist_by_id('playlist_id')
playlist = api.get_playlist_by_channel_id('channel_id')

playlistItems = api.get_playlist_items_by_playlist_id('playlist_id', max_results=20)

# Special
api_key = get_api_key()
bool = change_api_key('api_key')
```

## Pagination
```python
results = api.general_search('keyword', max_results=10, pageToken=PAGETOKEN)
videos = api.video_search('keyword', max_results=10, order=None, pageToken=PAGETOKEN)
videos = api.video_search_in_channel('keyword', 'channel_id', max_results=10, order=None, pageToken=PAGETOKEN)
playlistItems = api.get_playlist_items_by_playlist_id('playlist_id', max_results=20, pageToken=PAGETOKEN)
```

## Contributing
[https://github.com/ahmetkotan/yapi](https://github.com/ahmetkotan/yapi)

## Youtube Data API v3
[Youtube Data API v3 Doc](https://developers.google.com/youtube/v3/)
