# Final Project for Computing for Data Science at the Barcelona School of Economics

PopularityContest is a library for a machine learning model that predicts if a song is going to be popular in a certain country. 

Right now the model is specified for Spain. 

The code is divided in three folders: Load, Process, Model, and test.

Load:
contains our data acquistion files
 - spotify.py connects to the Spotify API in order to download songs and their data. 
 - data.py creates a Pandas DataFrame from data collected from the Spotify API

Process:
contains our feature engineering files
- feature1.py Creates the feature 'happy'
- feature2.py Creates the features 'HipHop', 'Reggaeton', 'Pop', and 'House/Electro/Techno'
- feature3.py Creates the features 'duration_s' and 'duration_m'

Model:
contains the files associated with our machine learning model. 
- best_model.py functions for assessing model accuracy
- split.py function for splitting the data into test and training sets

test:
contains the files used to test the preprocessing and feature engineering functions
- Load/
  - test_spotify.py tests the functions defined in the Spotify class
- Process/
  - test_features.py tests the feature creation functions


test.ipynb is where we run the model. 


To start contributing clone our repo and contact us to set up your configuration file. 

If you add new functions to the spotify.py or make a new feature (by making a new feature file) please add a unit test to the associated unit test files.
