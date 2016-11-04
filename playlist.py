##Get URIs from a spotify playlist.


import config

import spotipy
import spotipy.util as util


def getPlaylist():
    scope = 'user-library-read playlist-read-private'

    c = config.Configuration()


    token = util.prompt_for_user_token(c.user, scope,
                                       c.clientid, c.clientsecret,c.redirect)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(c.user)
        idDict = {playlist["name"]:playlist["id"] for playlist in playlists["items"]}
        names = [i for i in idDict.keys()]
        nameDict = {i:names[i] for i in range(len(names))}
        print("Please input the number of the playlist you want.")
        for i in range(len(names)):
            print("    "+str(i)+": "+nameDict[i])
        listID = idDict[nameDict[int(input("--> "))]]
        results = sp.user_playlist(c.user,listID,"tracks")
        outList=[]
        for i in results['tracks']['items']:
            timeTuple = msToTuple(i["track"]["duration_ms"])
            outList.append((i['track']['artists'][0]['name'],i['track']['name'], str(timeTuple[0])+":"+("0" if timeTuple[1]<10 else "")+str(timeTuple[1])+"."+str(timeTuple[2])))
        return outList
    
    else:
        return False

def msToTuple(ms):
    time_ms =  ms
    mod_ms = time_ms % 1000
    time_s = int((time_ms - mod_ms)/1000)
    mod_s = time_s % 60
    time_m = int((time_s - mod_s)/60)
    return (time_m,mod_s,mod_ms)


if __name__ == "__main__":
    print(getPlaylist())
