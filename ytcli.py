import yt_dlp as youtube_dl
import os
import platform
import setup
import mysql.connector

# Database connection details
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'ytcli_db'
}

# Determine the OS and set appropriate commands
osname = platform.system()
mpv = ""
pip = ""
clear = ""
if osname == "Linux":
    mpv = "mpv"
    pip = "pip3"
    clear = "clear"
elif osname == "Windows":
    mpv = ".\\mpv"
    pip = "pip"
    clear = "cls"

# Import and install dependencies
try:
    from youtubesearchpython import VideosSearch
    from pytube import Playlist
    hasmpv = len(os.popen(mpv + " --version").read())
    haspip = len(os.popen(pip + " --version").read())
    if hasmpv == 0 or haspip == 0:
        raise Exception
except:
    setup.install()
    from youtubesearchpython import VideosSearch
    from pytube import Playlist

# To manipulate data in database
def change(query, data=None):
    con = mysql.connector.connect(**db_config)
    cur = con.cursor()
    if data is None:
        cur.execute(query)
    else:
        cur.executemany(query, data)
    con.commit()
    cur.close()
    con.close()

# To fetch data from database
def fetch(query, data=None):
    con = mysql.connector.connect(**db_config)
    cur = con.cursor()
    if data is None:
        cur.execute(query)
    else:
        cur.execute(query, data)
    li = cur.fetchall()
    cur.close()
    con.close()
    return li

# To display menu
def menu(title, options):
    os.system(clear)
    for i, val in enumerate(options):
        print(str(i + 1) + "\t" + val)
    print("\q\tBack")
    choice = input(title)
    os.system(clear)
    if choice == "\q":
        return [choice, "Back"]
    return [choice, options[int(choice) - 1]]

# To search for a particular song
def search():
    while True:
        s = input("Search: ")
        if s == "\q":
            break
        else:
            videosSearch = VideosSearch(s, limit=50)
            r = videosSearch.result()
            disp_li = []
            li = []
            os.system(clear)

            for i in r["result"]:
                title = i["title"][:40]
                if len(title) < 40:
                    title = title + " " * (40 - len(title))
                duration = i["duration"]
                views = i["viewCount"]["short"]
                disp_li.append("{0}\t\t\t{1}\t\t{2}".format(title, duration, views))
                li.append(i["link"])

            # Sending data to display search details
            play(disp_li, li)

# To prompt the user to select a song
def play(disp_li, li):
    music = menu(title="Choose Song: ", options=disp_li)[0]
    if music == "\q":
        return
    else:
        choice = menu(title="Enter your choice: ", options=["Audio only mode", "Regular Mode"])[0]
        if choice == "\q":
            return
        print(disp_li[int(music) - 1])
        print("\n", li[int(music) - 1], "\n")
        if choice == "1":
            command = mpv + " {0} --no-video".format(li[int(music) - 1])
        elif choice == "2":
            command = mpv + " {0}".format(li[int(music) - 1])
        os.system(command)

# To add a new playlist
def addPlaylist():
    os.system(clear)
    name = input("Enter playlist name: ")
    link = input("Enter url: ")
    query = "CREATE TABLE IF NOT EXISTS Playlist(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), link TEXT)"
    change(query)
    data = [(name, link)]
    query = "INSERT INTO Playlist(name, link) VALUES(%s, %s)"
    change(query, data)

# To prompt the user to select a playlist
def getPlaylist():
    query = "SELECT name FROM Playlist"
    li = fetch(query)
    if len(li) == 0:
        print("No playlists found. Please add a playlist first.")
        addPlaylist()
        li = fetch(query)
    
    disp_li = [item[0] for item in li]
    playlist = menu(title="Choose playlist: ", options=disp_li)[1]
    if playlist == "Back":
        return False
    query = "SELECT link FROM Playlist WHERE name=%s"
    li = fetch(query, (playlist,))
    url = li[0][0]
    return url

# To prompt the user to select a playlist for deletion
def delPlaylist():
    link = getPlaylist()
    if link == False:
        return
    query = "DELETE FROM Playlist WHERE link=%s"  # Deleting playlist record from database
    change(query, [(link,)])

if __name__ == "__main__":
    while(True):
        choice = menu(title="Enter your choice: ", options=["Start Playlist", "Add Playlist", "Delete Playlist", "Search"])[0]
        if choice == "1":
            link = getPlaylist()
            if link != False:
                mode = menu(title="Choose mode: ", options=["Audio only mode", "Regular Mode"])[0]
                if mode == "1":
                    command = mpv+" "+link+" --no-video --shuffle"
                elif mode == "2":
                    command = mpv+" "+link+" --shuffle"
                else:
                    continue
                os.system(command)
        elif choice == "2":
            addPlaylist()
        elif choice == "3":
            delPlaylist()
        elif choice == "4":
            search()
        elif choice == "\q":
            exit()
