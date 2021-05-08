import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
from dataclasses import dataclass

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

PLAYLIST_ID_OF_NEW_SONGS = '6qZnImkqxbRtL9FiwqHkGK'

@dataclass
class TrackData():
    name: str = ''
    uri: str = ''
    preview_url: str = ''
    popularity: str = ''

    def from_spotify_track(spotify_track: any):
        track_data = TrackData()
        track_data.name = spotify_track['name']
        track_data.uri = spotify_track['uri']
        track_data.preview_url = spotify_track['preview_url']
        track_data.popularity = spotify_track['popularity']
        return track_data

def get_random_track():
    # Make callout to spotify
    playlist_of_new_songs = sp.playlist(PLAYLIST_ID_OF_NEW_SONGS)

    # Parse result for track
    track_items = (playlist_of_new_songs['tracks'])['items']
    random_track_item = random.choice(track_items)
    random_track = random_track_item['track']

    # Convert to easy to use object
    return TrackData.from_spotify_track(random_track)
