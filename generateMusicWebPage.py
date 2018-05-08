# read music from music.json
import json

def big2Small(song):
    return {"title":song['song']['title'],
            "artist":song['artist']['name']}

def songListToHTMLTable(songs):
    answer="<table>\n"+songTableHeader()
    for song in songs:
        answer += song2HTMLTableRow(song)
    answer += "</table>\n"
    return answer

def songTableHeader():
    return ("<tr>\n"+
            "<th> Song Title </th>"+
            "<th> Artist Name </th>"+
            "</tr>\n")

def song2HTMLTableRow(song):
    return("<tr>\n" +
           "<td>"+song['song']['title']+"</td>"+
           "<td>"+song['artist']['name']+"</td>"+
           "</tr>\n")

def writeWebPage(filename,content, title):
    with open(filename,'w') as webpage:
        webpage.write("<!DOCTYPE>")
        webpage.write("<html>")
        webpage.write("<title>")
        webpage.write(title)
        webpage.write("</title>")
        webpage.write(content)
        webpage.write("</html>")

if __name__=="__main__":
    with open('music.json.txt') as json_data:
        songs=json.load(json_data)
    print("The variable songs now contains all the data")

    print("the variable songs is a list of big complicated dict")
    print("We'd like something easier to work with")
    print("The function big2Small(song) will turn a big song dict into smaller")
    writeWebPage("fiveSongs.html", songListToHTMLTable(songs[5:10]), "five songs")

    
