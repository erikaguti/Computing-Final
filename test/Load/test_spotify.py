import unittest
import pandas as pd
from PopularityContest.Load.spotify import Spotify

sp = Spotify('ES')


def test_getCategories():
    'Main point of this function is to get categories that are not the Top Charts ones'
    categorytest = ['toplists']
    categories = sp.getCategories()
    assert categorytest not in categories

def test_getPlaylists():
    'test we got ids from API and that the limit parameter is working'
    categories = ['0JQ5DAqbMKFx0uLQR2okcc']
    playlists = sp.getPlaylists(categories, 5)
    print(playlists)
    assert len(playlists) == 5

def test_getSongs():
    'test we got ids from API and that the limit parameter is working'
    playlists = ['37i9dQZF1DWXRqgorJj26U']
    songs = sp.getSongs(playlists, limit = 1)
    assert len(songs) == 1

def test_getSongFeatures():
    'Test we got only 3 items back and that there are no None types'
    songstest = ['254bXAqt3zP6P50BdQvEsq', '40riOy7x9W7GXjyGp4pjAv', '6KTv0Z8BmVqM7DPxbGzpVC']
    features = sp.getSongFeatures(songstest)
    assert len(features) == 3 and None not in features

def test_idstringer():
    teststrings = ['computing', 'for', 'data', 'science', 'final']
    expectedoutput = 'computing,for,data,science,final'
    output = sp.idstringer(teststrings)
    assert expectedoutput == output

