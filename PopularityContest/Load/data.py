import spotify
import pandas as pd

'This code creates the base dataframe that will be used in our model'

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

'Bring it all together'
Top50 = pd.DataFrame(Top50songfeatures)
NotTop50 = pd.DataFrame(notTop50songfeatures)

Top50['Top50'] = 1
NotTop50['Top50'] = 0

data = pd.concat([Top50, NotTop50])

data.drop_duplicates(subset='id', inplace=True, ignore_index=True)









