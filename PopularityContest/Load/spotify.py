import spotipy
import config
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify():
    def __init__(self,countrycode):
        'country code must be an ISO 3166-1 alpha-2 country code'
        self.country = countrycode
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=config.id, client_secret=config.secret))
    
    def getCategories(self):
        categories = self.spotify.categories(country=self.country, locale='en')
        categoryids = []
        for category in categories['categories']['items']:
            if category['id'] != 'toplists':
                categoryids.append(category['id'])
        return categoryids
    
    def getPlaylists(self, categoryids, limit = 20, top50 = False):
        playlistids = []
        try:
            for id in categoryids:
                playlists = self.spotify.category_playlists(category_id = id, country=self.country, limit = limit)
                for playlist in playlists['playlists']['items']:
                    if top50:
                        if 'Global' not in playlist['name'] and 'Top' in playlist['name'] and '50' in playlist['name']:
                            playlistids.append(playlist['id'])
                    else:
                        playlistids.append(playlist['id'])
        except:
                pass
        return playlistids
    
    def getSongs(self, playlistids, limit = 50, Top50 = False):
        trackids = []
        for playlistid in playlistids:  
            playlisttracks = self.spotify.playlist_items(playlistid, fields='items(track.id)', limit = limit)
            for track in playlisttracks['items']:
                trackids.append(track['track']['id'])
        return trackids
    
    def getSongFeatures(self, trackids, offset = 0, limit = 100):
        features = []
        songs = len(trackids)
        print("num songs:", songs)
        while songs > 100:
            features.extend(self.spotify.audio_features(self.idstringer(trackids[offset:limit])))
            offset = offset + 100
            limit = limit + 100
            songs = songs - 100
        else:
            features.extend(self.spotify.audio_features(self.idstringer(trackids[offset:limit+songs])))
        return features

    def idstringer(self, ids):
        idstr = ''
        for id in ids:
            if id == ids[-1]:
                idstr = idstr + id
            else:
                idstr = idstr + id + ','
        return idstr

    


    
















