##Get track length from spotify URI

import requests, json

def URIToLength(uri):
    url = "https://api.spotify.com/v1/tracks/"+uri
    r = requests.get(url)
    t = json.loads(r.text)
    time_ms =  int(t["duration_ms"])
    mod_ms = time_ms % 1000
    time_s = int((time_ms - mod_ms)/1000)
    mod_s = time_s % 60
    time_m = int((time_s - mod_s)/60)
    return (time_m,mod_s,mod_ms)


if __name__=="__main__":
    uri = "16w8ZGVSjI4TlTLV8VimBY"
    print(URIToLength(uri))
