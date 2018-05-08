import json
import random
import pprint

with open('music.json') as json_data:
    songs = json.load(json_data)

##print("len(songs)=",len(songs))
##print("type(songs)=",type(songs))

# Choose a random sample

sampleSongs = random.sample(songs,10)

def bigSong2SmallSong(bigSong):
    return {
     'song_title':bigSong['song']['title'],
     'album': bigSong['release']['name'],
     'artist': bigSong['artist']['name'],
     'year': bigSong['song']['year'],
     'tempo': bigSong['song']['tempo'],
     'terms': bigSong['artist']['terms']
    }

def smallSongListToLenList(smallSongList):
    lenList= []
    for s in smallSongList:
        lenList.append(  len(s['song_title']) )
    return lenList

def printSmallSongTable(smallSongs):
    " assuming songs with keys from bigSong2SmallSong, print table "
    for s in smallSongs:
        #print(s['song_title'],s['year'])
        if len(s['song_title'])>30:
            ellipsis = "..."
        else:
            ellipsis = ""
        print('{:30}{:3} {:4}'.format(s['song_title'][0:30],ellipsis,s['year']))
  
# Conrad's original version
##smallSongs = []
##for song in sampleSongs:
##    smallSong = bigSong2SmallSong(song)
##    smallSongs.append(smallSong)

# Bowen's version
smallSongs = []
for song in sampleSongs:
    smallSongs.append(bigSong2SmallSong(song))

printSmallSongTable(smallSongs)

#for song in smallSongs:
#    pprint.pprint(song)

allSongsAsSmallSongs = []
for song in songs:
    allSongsAsSmallSongs.append(bigSong2SmallSong(song))

allLengths = smallSongListToLenList(allSongsAsSmallSongs)

longestSongTitleLen = max(allLengths)

print("The longest song title is of length: ",longestSongTitleLen)


##for s in songs:
##    if len(s['song']['title'])==longestSongTitleLen:
##        pprint.pprint(s)
