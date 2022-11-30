import spotipy, json
from spotipy.oauth2 import SpotifyOAuth
import creds 
import collections

scope = "playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.client_id, client_secret= creds.client_secret, redirect_uri=creds.redirect_url, scope=scope))


# this is able to get the artist id form a playlist
#for i in range(100):
#    artist_list.append(playlist['tracks']['items'][i]['track']['artists'][0]['id'])
artist_list = []
playlist_url = input('Input Playlist URL (e.g. https://open.spotify.com/playlist/6eV2eTfwDzuM0U4ZzIQKdf?si=28272a46cc464d2a): ').split('/')[4].split('?')[0]

playlist = sp.playlist_items(playlist_url)
for i in playlist['items']:
    for j in i['track']['artists']:
        artist_list.append(j['id'])


unqiue_artists = list(set(artist_list))
print(len(unqiue_artists))

# for each artist count the genre
# we will create a dictionary object with a count for this
genre_list = []
artist_list = []


for artist_id in unqiue_artists:
    artist = sp.artist(artist_id)
    #print(artist['name'])
    #print(artist['genres'])

    for genre in artist['genres']: 
        genre_list.append(genre)

    print(f"{artist['name']}: {artist['genres']}")

counted_list = collections.Counter(genre_list)
print(counted_list)
            









#artist = sp.artists(['0k17h0D3J5VfsdmQ1iZtE9'])
#print(artist)
