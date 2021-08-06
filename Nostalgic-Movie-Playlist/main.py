choice=input("what year you would like to travel to in YYY-MM-DD format: ")
from bs4 import BeautifulSoup
import requests
f = open("website.html", "r")
contents=f.read()
soup=BeautifulSoup(contents,'html.parser')
print(soup.title.string)

response=requests.get(f"https://www.billboard.com/charts/hot-100/{choice}")
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage,"html.parser")
texts=soup.find_all(class_ ="chart-element__information__song text--truncate color--primary")
song_list=[t.getText() for t in texts]
print(song_list)

import spotipy
from spotipy.oauth2 import SpotifyOAuth
def GetTrackIDs(sample_data):
    #Get Spotify track ids for samples
    track_ids = []
    #Track Info Box Flow
    for i in range(len(sample_data)):
        results = sp.search(q=f"{sample_data['title'][i]} {sample_data['artist'][i]} ", limit=1, type='track') 
        if results['tracks']['total'] == 0:
           #if track isn't on spotify as queried, go to next track
            print("Couldn't find track ID")
            continue
        else:
             track_ids.append(results['tracks']['items']['id']) 
             
    #Track Annotation Flow
   
    return track_ids

def GetPlaylistID(username, playlist_name):
    playlist_id = ''
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:  # iterate through playlists I follow
        if playlist['name'] == playlist_name:  # filter for newly created playlist
            playlist_id = playlist['id']
    return playlist_id
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="[YOUR KEY]",
        client_secret="[YOUR KEY]",
        show_dialog=True,
        cache_path="token.txt"
    )
)



user_id = sp.current_user()["id"]
playlist_name = f"Billiboard Top 100 on {choice}"    
sp.user_playlist_create(user_id, name=playlist_name,public=False)
track_ids=GetTrackIDs(song_list)
playlist_id=GetPlaylistID(user_id,playlist_name)
sp.user_playlist_add_tracks(user_id, playlist_id, track_ids)
print(user_id)
