##Get URIs from a spotify playlist.

import spotipy
import spotipy.util as util

scope = 'user-library-read'

username = input("What's your username? ")

token = util.prompt_for_user_token(username,scope)

if token:
    sp = spotipy.Spotify(auth=token)
    for playlist in playlists['items']:
        print (playlist['name'] + playlist['id'])
