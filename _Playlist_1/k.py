from flask import Flask, request, jsonify
from linked_list import SongsList

app = Flask(__name__)
app.json.sort_keys = False


global_playlist_id = 0
app_playlists = {}


@app.route("/")
def home():
    return "Welcome!"

### PLAYLIST ENDPOINTS

@app.route("/playlist/create", methods=["POST"])
def create_playlist():
    '''Creates playlist with empty songs list.'''
    try:
        playlist_data = request.json
        global global_playlist_id
        app_playlists[global_playlist_id] = SongsList(playlist_data['name'], playlist_data['description'])
        global_playlist_id += 1
        return jsonify({"Success!": f"New playlist added with ID #{global_playlist_id - 1}."}), 201
    except Exception as e:
        return jsonify({"Excpetion": f"Something went wrong: {e}"}), 400


@app.route("/playlist/<int:playlist_id>", methods=["GET"])
def get_playlist(playlist_id):
    '''Fetch playlist by id number'''
    if playlist_id in app_playlists.keys():
        display_playlist = { 
            "Playlist ID" : f"{playlist_id}",
            "Name" : f"{app_playlists[playlist_id].name}",
            "Description" : f"{app_playlists[playlist_id].description}",
            "Songs" : app_playlists[playlist_id].print_songs()
        }
        return display_playlist
    else:
        return f"No playlist found with ID #{playlist_id}", 404


@app.route("/playlist/update/<int:playlist_id>", methods=["PUT"])
def update_playlist(playlist_id):
    '''Update name and description for playlist.'''
    try:
        if playlist_id in app_playlists.keys():
            new_data = request.json
            app_playlists[playlist_id].name = new_data['name']
            app_playlists[playlist_id].description = new_data['description']
            return jsonify({"Success!": f"Playlist '{new_data['name']}' updated!"}), 200
        else:
            return f"No playlist found with ID #{playlist_id}", 404
    except Exception as e:
        return jsonify({"Excpetion": f"Something went wrong: {e}"}), 400


@app.route("/playlist/delete/<int:playlist_id>", methods=["DELETE"])
def delete_playlist(playlist_id):
    '''Delete playlist from collection.'''
    try:
        if playlist_id in app_playlists.keys():
            del app_playlists[playlist_id]
            return jsonify({"Success!": f"Playlist deleted!"}), 200
        else:
            return f"No playlist found with ID #{playlist_id}", 404
    except Exception as e:
        return jsonify({"Excpetion": f"Something went wrong: {e}"}), 400


### SONG ENDPOINTS

@app.route("/playlist/<int:playlist_id>/add_song", methods=["POST"])
def add_song(playlist_id):
    '''Creates song and adds to specified playlist.'''
    try:
        if playlist_id in app_playlists.keys():
            song_data = request.json
            app_playlists[playlist_id].add_song(song_data['title'], song_data['artist'], song_data['album'], song_data['genre'])
            return jsonify({"Success!": f"'{song_data['title']} added to playlist '{app_playlists[playlist_id].name}'"}), 201
        else:
            return f"No playlist found with ID #{playlist_id}", 404
    except Exception as e:
        return jsonify({"Excpetion": f"Something went wrong: {e}"}), 400


@app.route("/playlist/<int:playlist_id>/remove_song/<int:song_id>", methods=["DELETE"])
def remove_song(playlist_id, song_id):
    '''Remove specified song by ID from playlist by ID.'''
    try:
        if playlist_id in app_playlists.keys():
            if app_playlists[playlist_id].remove_song(song_id):
                return jsonify({"Success!": f"Song #{song_id} removed from playlist '{app_playlists[playlist_id].name}'"}), 201
            else: 
                return f"No song with ID #{song_id} found in playlist", 404
        else:
            return f"No playlist found with ID #{playlist_id}", 404
    except Exception as e:
        return jsonify({"Excpetion": f"Something went wrong: {e}"}), 400


@app.route("/playlist/<int:playlist_id>/search", methods=["GET"])
def search_song(playlist_id):
    '''Search for song within specified playlist '''
    try:
        if playlist_id in app_playlists.keys():
            search = request.args.get('search')
            if not search:
                return {"Error" : "Must include the 'search' query parameter."}
            prop = request.args.get('property')
            if not prop:
                prop = "song_id"
            if prop is "song_id":
                search = int(search)

            search_result = app_playlists[playlist_id].search_songs(search, prop)
            if search_result:
                display_song = {
                    "Song ID" : search_result.song_id,
                    "Title" : search_result.title,
                    "Artist" : search_result.artist,
                    "Album" : search_result.album,
                    "Genre" : search_result.genre
                }

                return display_song
            else: 
                return f"No song in playlist found with search '{search}' through property '{prop}'", 404
        else:
            return f"No playlist found with ID #{playlist_id}", 404
    except Exception as e:
        return jsonify({"Excpetion": f"Something went wrong: {e}"}), 400
