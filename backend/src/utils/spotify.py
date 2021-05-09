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

    def from_spotify_track(spotify_track: any):
        track_data = TrackData()
        track_data.name = spotify_track['name']
        track_data.uri = spotify_track['uri']
        track_data.preview_url = spotify_track['preview_url']
        return track_data

def get_random_track():
    # Make callout to spotify
    playlist_of_new_songs = sp.playlist(PLAYLIST_ID_OF_NEW_SONGS)

    # Parse result for track
    track_items = (playlist_of_new_songs['tracks'])['items']
    random_track_item = random.choice(track_items)
    random_track = random_track_item['track']

    # If the track is invalid, retry with another random track
    track_data = TrackData.from_spotify_track(random_track)
    if is_track_valid(track_data):
        # Convert to easy to use object
        return track_data
    else:
        return get_random_track()

def is_track_valid(track_data: TrackData):
    # Validate that all required fields are present
    return (
        track_data.name != None and
        track_data.uri != None and 
        track_data.preview_url != None
    )
