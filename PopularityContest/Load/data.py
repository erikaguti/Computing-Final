import spotipy
import config
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify():
    def __init__(self,countrycode):
        'country must be an ISO 3166-1 alpha-2 country code'
        self.country = countrycode
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=config.id, client_secret=config.secret))
        self.playlistsamplesize = 0
        self.Top50 = []
    
    def getCategories(self):
        categories = self.spotify.categories(country=self.country, locale='en')
        categoryids = []
        for category in categories['categories']['items']:
            if category['id'] != 'toplists':
                categoryids.append(category['id'])
        return categoryids
    
    def getPlaylists(self, categoryids, limit, top50 = False):
        playlistids = []
        for id in categoryids:
            playlist = self.spotify.category_playlists(category_id = id, country='ES', limit=5)
            for playlist in playlist['playlists']['items']:
                if top50:
                    if 'Global' not in item['name'] and 'Top' in item['name'] and '50' in item['name']:
                        playlistids.append(item['id'])
                else:
                    self.playlistsamplesize = self.playlistsamplesize + 1
                    playlistids.append(playlist['id'])
        return playlistids
    
    def getPlaylistTrackIDs(self, idlist, limit, Top50 = False):
        for id in idlist:  
            playlisttracks = self.spotify.playlist_items(idlist, fields='items(track.id)', limit = limit)
        trackids = []
        for track in playlisttracks['items']:
            trackids.append(track['track']['id'])
        if Top50:
            self.Top50 = trackids
        return trackids
    
    def getSongFeatures(self, trackids, offset = 0, limit = 100):
        features = []
        songs = len(trackids)
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

    


    
















