from api_keys import read_from_api_file
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

client_id = read_from_api_file(".api_keys.json", "ClientID")
client_secret = read_from_api_file(".api_keys.json", "ClientSecret")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_to_text(playlist_link, out_file):
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    tracks = [x["track"] for x in sp.playlist_tracks(playlist_URI)["items"]]

    for i in range(len(tracks)):
        try:
            track_string = f'{i+1}. {tracks[i]["name"]} --- {tracks[i]["artists"][0]["name"]} --- {tracks[i]["album"]["name"]} \n'

            file = open(out_file, "a")
            file.write(track_string)
            file.close()

        except:
            print("An error has occured with a track!")

playlist_link = sys.argv[1]
out_file = sys.argv[2] 

get_playlist_to_text(playlist_link, out_file)