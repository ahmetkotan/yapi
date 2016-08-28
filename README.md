yapi
===================
#### Python - Youtube Data API v3

**yapi** is a simple client api for youtube.It uses [Youtube Data API v3](https://developers.google.com/youtube/v3/).Before you can use, you must a create project in [here](https://console.developers.google.com/apis/api/youtube/overview).

## Installation
``` sudo pip install yapi
```

## Using
```
import yapi
api = yapi.YoutubeAPI('api_key')
```

## References
```
videos getVideoInfo('video_id')

search generalSearch('keyword', max_results=10)
search videoSearch('keyword', max_results=10)
search videoSearchInChannel('keyword', 'channel_id', max_results=10)

channel getChannelByName('channel_name')
channel getChannelById('channel_id')

playlist getPlaylistById('playlist_id')
playlist getPlaylistByChannelId('channel_id')

playlistItems getPlaylistItemsByPlaylistId('playlist_id', max_results=20)

# Special
api_key getApiKey()
changeApiKey('api_key')
```

## Contributing
[https://github.com/ahmetkotan/yapi](https://github.com/ahmetkotan/yapi)

## Youtube Data API v3
[Youtube Data API v3 Doc](https://developers.google.com/youtube/v3/)
