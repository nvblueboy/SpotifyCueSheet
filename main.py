##Output spotify playlist info into a CSV file to import into excel.

import playlist

def listToFile(filename):
    songList = playlist.getPlaylist()

    outString = ""
    for i in songList:
        outString += i[0]+","+i[1]+","+i[2]+"\n"
    fileHandle = open(filename,"w")
    fileHandle.write(outString)
    fileHandle.close()

if __name__=="__main__":
    file = input("Where do you want to put this file?")
    listToFile(file)
