import spotify
import pandas as pd


sp = spotify.Spotify('ES')

'Get Playlists'
top50playlists = sp.getPlaylists(['toplists'], top50=True)
cat = sp.getCategories()
notTop50playlists = sp.getPlaylists(cat)

'Get Songs'
Top50songs = sp.getSongs(top50playlists)
notTop50songs = sp.getSongs(notTop50playlists, 10)

'Get Song Features'
Top50songfeatures = sp.getSongFeatures(Top50songs)
notTop50songfeatures = sp.getSongFeatures(notTop50songs)

Top50 = pd.DataFrame(Top50songfeatures)
NotTop50 = pd.DataFrame(notTop50songfeatures)

Top50['Top50'] = 1
NotTop50['Top50'] = 0

datadraft = pd.concat([Top50, NotTop50])

datadraft['duplicates'] = datadraft.duplicated(subset=['id'])

for i in range(0, len(notTop50songfeatures)):
    if notTop50songfeatures[i] is None:
        print(i)


notTop50songs[232]

sp.spotify.audio_features(notTop50songs[232])










