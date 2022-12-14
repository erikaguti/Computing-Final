import spotipy
import config
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

charts = pd.read_csv('charts.csv')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=config.id, client_secret=config.secret))

Top50 = spotify.category_playlists(category_id = 'toplists', country='ES')

playlistids = []
for item in Top50['playlists']['items']:
    if 'Global' not in item['name'] and 'Top' in item['name'] and '50' in item['name']:
        playlistids.append(item['id'])


for playlistid in playlistids:  
    playlisttracks = spotify.playlist_items(playlistid, fields='total, items(track.id)', limit = 50)


trackids = []
for track in playlisttracks['items']:
    trackids.append(track['track']['id'])


audiofeatures = spotify.audio_features(trackids)

songfeatures = pd.DataFrame(audiofeatures)


'''
Audio analysis code draft (if we want to add more features)
audioanalysis = {}
for id in songfeatures.id:
    audio = spotify.audio_analysis(id)
    audioanalysis.update({id: audio['track']})

audioanalysisdf = pd.DataFrame()
for item in audioanalysis:
    audioanalysis[item]
'''







