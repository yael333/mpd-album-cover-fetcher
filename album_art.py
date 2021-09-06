import pylast
import socket
import urllib.request
import traceback

username = ""
password_hash = pylast.md5("")
api_key=""
api_secret=""

network = pylast.LastFMNetwork(
    api_key=api_key,
    api_secret=api_secret,
    username=username,
    password_hash=password_hash)


HOST = '127.0.0.1'
PORT = 65432

last_split = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    track_string = str(data.decode('utf-8').strip())
                    split = track_string.split("---")
                    split[0] = split[0].split(";")[0]
                    print(split)
                    if (last_split != split):
                        album = network.get_album(split[0], split[1])
                        image = album.get_cover_image()
                        if (image):
                            urllib.request.urlretrieve(image, f"/tmp/album_cover.jpg")
                    last_split = split
                except Exception as e:
                    print(e)
