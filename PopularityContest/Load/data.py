import spotipy
import config
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials


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


Top50features = spotify.audio_features(trackids)

songfeatures = pd.DataFrame(Top50features)


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


categories = spotify.categories(country='ES', locale='en')

categoryids = []
for category in categories['categories']['items']:
    if category['id'] != 'toplists':
        print(category['name'], category['id'])
        categoryids.append(category['id'])

count = 0
playlistids = []
for id in categoryids:
    playlist = spotify.category_playlists(category_id = id, country='ES', limit=5)
    playlists = playlist['playlists']['items']
    for item in playlists:
        count = count + 1
        playlistids.append(item['id'])

tracks = []
for id in playlistids:
    playlisttracks = spotify.playlist_items(playlistid, fields='total, items(track.id)', limit = 5)
    tracks.extend(playlisttracks['items'])

ids = []
for track in tracks:
    ids.append(track['track']['id'])


NotTop50features = []
songs = len(ids)
print(songs)
offset = 0
limit = 100
while songs > 100:
    NotTop50features.extend(spotify.audio_features(idstringer(ids[offset:limit])))
    offset = offset + 100
    songs = songs - 100
    limit = limit + 100
else:
    NotTop50features.extend(spotify.audio_features(idstringer(ids[offset:limit+songs])))

def idstringer(ids):
    idstr = ''
    for id in ids:
        if id == ids[-1]:
            idstr = idstr + id
        else:
            idstr = idstr + id + ','
    return idstr


songfeatures['Top50'] = 1
notTop50 = pd.DataFrame(list(filter(lambda i:not(i == None), NotTop50features)))

notTop50['Top50'] = 0

pd.concat([songfeatures, notTop50]).to_csv('songfeatures.csv')












