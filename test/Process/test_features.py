import unittest
import pandas as pd
from PopularityContest.Process.feature1 import *
from PopularityContest.Process.feature2 import *
from PopularityContest.Process.feature3 import *
#from PopularityContest.Process import feature1, feature2, feature3

# https://github.com/4Freye/Computing-HW5/blob/master/test/test_hw5.py

class TestFeatures(unittest.TestCase):
    def test_feature1(self):
        test_df = pd.DataFrame({'valence': [0.4, 0.6, 0.8]})
        expected_df = pd.DataFrame({'valence': [0.4, 0.6, 0.8], 'happy': [0, 1, 1]})
        result_df = feature1(test_df)
    
        assert result_df.equals(expected_df)

    def test_genre_function(self):
    #create a dataframe
        df = pd.DataFrame({"tempo": [90, 100, 140, 85, 95]})
    #expected output
        expected_output = pd.DataFrame({"tempo": [90, 100, 140, 85, 95], 
                                    "HipHop": [1, 0, 0, 1, 1],
                                    "Reggaeton": [1, 1, 0, 0, 0],
                                    "Pop": [0, 1, 1, 0, 0],
                                    "House/Electro/Techno": [1, 1, 1, 0, 0]})
    #call the function
        result = genre(df)
    #compare expected output and result
        self.assertEqual(expected_output.equals(result), True) 

    def setUp(self):
        self.df = {'duration_ms': [1000, 3000, 60000, 90000]}
    
    def test_time_seconds(self):
        result = time(self.df, 'seconds')
        self.assertEqual(result, {'duration_s': [1.0, 3.0, 60.0, 90.0]})
        
    def test_time_minutes(self):
        result = time(self.df, 'minutes')
        self.assertEqual(result, {'duration_m': [0.016666666666666666, 0.05, 1.0, 1.5]})
        
    def test_time_invalid(self):
        result = time(self.df, 'hours')
        self.assertEqual(result, "Please enter a valid time unit")

class TestFeatures(unittest.TestCase):
    def test_feature1(self):
        self.test_df = pd.DataFrame({'valence': [0.4, 0.6, 0.8]})
        self.expected_df = pd.DataFrame({'valence': [0.4, 0.6, 0.8], 'happy': [0, 1, 1]})
        self.result_df = feature1(self.test_df)

        self.assertTrue(self.result_df.equals(self.expected_df))

    def test_genre_function(self):
    #create a dataframe
        df = pd.DataFrame({"tempo": [90, 100, 140, 85, 95]})
    #expected output
        expected_output = pd.DataFrame({"tempo": [90, 100, 140, 85, 95], 
                                    "HipHop": [1, 0, 0, 1, 1],
                                    "Reggaeton": [1, 1, 0, 0, 0],
                                    "Pop": [0, 1, 1, 0, 0],
                                    "House/Electro/Techno": [1, 1, 1, 0, 0]})
    #call the function
        result = genre(df)
    #compare expected output and result
        self.assertTrue(expected_output.equals(result)) 

    def setUp(self):
        self.df = {'duration_ms': [1000, 3000, 60000, 90000]}
    
    def test_time_seconds(self):
        result = time(self.df, 'seconds')
        self.assertEqual(result, {'duration_s': [1.0, 3.0, 60.0, 90.0]})
        
    def test_time_minutes(self):
        result = time(self.df, 'minutes')
        self.assertEqual(result, {'duration_m': [0.016666666666666666, 0.05, 1.0, 1.5]})
        
    def test_time_invalid(self):
        result = time(self.df, 'hours')
        self.assertEqual(result, "Please enter a valid time unit")