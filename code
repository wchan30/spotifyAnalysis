from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json
from util import track_feature_df
from util import df_heatmap
from util import df_pairplot
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# All functions relied on the spotify api documentation
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-Type':  'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    result = post(url, headers = headers, data = data)
    json_res = json.loads(result.content)
    token = json_res['access_token']
    return token

def get_auth_header(token):
    return {'Authorization': 'Bearer ' + token}


def get_playlist(token,playlist_id):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}?fields=tracks.items%28track%28name%2Cid%29%29'
    headers = get_auth_header(token)
    result = get(url,headers = headers)
    json_result = json.loads(result.content)['tracks']
    return json_result

token = get_token()
# Searched up Spotify's Top 50 playlist and found the playlist ID from the URL link
# ID can be changed to any playlist the user desires
songs = get_playlist(token,'37i9dQZF1DXcBWIGoYBM5M')

# Filtered the json_result to get the top ten songs using list/dic comprehensions
top_ten_song = [item['track']['name'] for item in songs['items']][:10]
top_ten_song_id = [item['track']['id'] for item in songs['items']][:10]

# After extracting the IDs, I needed to concatenate all of it into a string
# However, the url link is invalid as each id were seperated by "%2C"
# Simple for loop to add the necessary string
track_id = ''
for i in top_ten_song_id:
    track_id += i + '%2C'
# Last playlist ID didn't need to be concatendated so a basic string manipulation to remove it
track_id = track_id[:-3]


def get_audio_features(track_id):
    url = f'https://api.spotify.com/v1/audio-features?ids={track_id}'
    headers = get_auth_header(token)
    result = get(url,headers = headers)
    json_result = json.loads(result.content)['audio_features']
    return json_result

audio_features = get_audio_features(track_id)
# Filtered the json_result into key features that I assumed was impactful
filtered_features = [{key: track[key] for key in ['acousticness','danceability','duration_ms','energy','instrumentalness','key','loudness','mode','tempo','time_signature','valence']} for track in audio_features]

# Used the zip function to pair the song to its correlating audio features
# Used the dict function to create a dictionary where the key is the song and the value is the audio features
track_filtered_features = dict(zip(top_ten_song,filtered_features))

# Transformed the dictionary into a Pandas Dataframe
# Imported a function from the Util file
dataframe = track_feature_df(track_filtered_features)

# Show the correlation matrix to get a general idea
print(dataframe.corr())
# From the Util file, using the heatmap function
df_heatmap(dataframe)
df_pairplot(dataframe)

# Based on the results, we can strongly conclude that there are weak correlation across the features
# There are some positive correlation such as loudess and energy, but that is trivial as louder songs tend to bring more energy
# Weak correlation can be due to different genre of songs
# Since there are weak correlations between songs, a follow-up question is whether the song is popular because of the specific artist?
#
