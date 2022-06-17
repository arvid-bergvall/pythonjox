import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

#funkar inte av nån anledning att sätta environment variables
client_id = 'e52866d90e6f4ad1a4f9a01d7cc29adc'
client_secret = 'cbe0798595c844fb8a75c591051d0fc8'

# profile_uri = 'https://open.spotify.com/user/21xubhaa5hc3p7vswrjrcepyi?si=f7ceb77e6e794ecf'
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth( client_id = client_id, 
                                                client_secret = client_secret, 
                                                redirect_uri= "http://localhost:8080", 
                                                scope=scope, 
                                                open_browser=False))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
