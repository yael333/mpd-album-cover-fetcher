# mpd-album-cover-fetcher
Simple socket server that fetches album covers through LastFM written in Python.

## About
This project is intended to retrieve album covers for your currently playing track in [MPD](https://www.musicpd.org/). It is implemented in two parts:
* `album_art.py`, a python socket server which recieves info about currently playing tracks and downloads the fitting album cover.
* `client.sh`, a script which sends the server that info, which you will set up your MPD client to run on a track change.

## Dependencies
* [python](https://www.python.org/) and [pylast](https://github.com/pylast/pylast), the scripting language the server is written in and the required module for Last.fm API integration.
* A [Last.fm](https://www.last.fm) account and [API application](https://www.last.fm/api).
* [mpc](https://musicpd.org/clients/mpc/), used in the client script which sends currently playing track info to the python server
* [netcat](https://nmap.org/ncat/), used by the client script to send the currently playing track info to the server.

## Setup
Find `album_art.py` lines 6 to 9:
```
username = ""
password_hash = pylast.md5("")
api_key=""
api_secret=""
```
Using your favorite text editor, add your Lastfm account and API info here.

### The next section is written for [ncmpcpp](https://github.com/ncmpcpp/ncmpcpp) and will vary for different MPD clients

Next, add the following line to `~/.ncmpcpp/config`:
```
execute_on_song_change=/path/to/client.sh
```
Obviously, you need to point that line to the location of the `client.sh` script.
If you don't have a `~/.ncmpcpp/config`, make one, and ncmpcpp will use it as its default config.

## Usage
Run `album_art.py`. Now when you play a track on your MPD client, its album art will be written to `/tmp/album_cover.jpg`.
You can use [feh](https://feh.finalrewind.org) or your image viewing program of choice to view the image.


## Configuration
The following values can be configured based on your preferences.
* The server runs on port 65432 by default. You can change this in `album_art.py` at line 19, but make sure you modify `client.sh` as well.
* The default image path is `/tmp/album_cover.jpg`, but you can modify this at line 42 of `album_art.py`.
