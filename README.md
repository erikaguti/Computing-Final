# Final Project for Computing for Data Science at the Barcelona School of Economics

PopularityContest is a library for a machine learning model that predicts if a song is going to be popular in a certain country. 

Right now the model is specified for Spain. 

The code is divided in three folders: Load, Process, and Model

Load:
contains our data acquistion files
 - spotify.py connects to the Spotify API in order to download songs and their data. 
 - data.py creates a Pandas DataFrame from data collected from the Spotify API

Process:
contains our feature engineering files
- feature1.py Creates the feature 'happy'
- feature2.py Creates the features 'HipHop', 'Reggaeton', 'Pop', and 'House/Electro/Techno'
- feature3.py Creates the features 'duration_s' and 'duration_m'

Model
contains the files associated with our machine learning model. 
- best_model.py functions for assessing model accuracy
- split.py function for splitting the data into test and training sets



