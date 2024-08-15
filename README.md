Project: Playlist Management API

Author: Reggie Joseph


This application simulates a collection of playlists and the songs they store. I began this application with a comment block analyzing which data structures would be most effective for storing, adding to, and searching for songs. Ultimately, I chose a dictionary of doubly linked lists to represent each playlist, with songs as nodes.

This application includes several endpoints for managing playlists and songs:

Playlist Endpionts

Create Playlist /playlist/create - Create an empty playlist with a name and description. playlist_id is automatically assigned.
Get Playlist /playlist/<int:playlist_id> - Fetch playlist by playlist_id.
Update Playlist /playlist/update/<int:playlist_id> - Update name and description for playlist at playlist_id.
Delete Playlist /playlist/delete/<int:playlist_id> - Remove playlist from collection using playlist_id.
Song Endpoints

Add Song /playlist/<int:playlist_id>/add_song - Add a song with title, artist, album, and genre to the playlist with playlist_id. song_id is automatically assigned.
Remove Song /playlist/<int:playlist_id>/remove_song/<int:song_id> - Remove song with song_id from playlist_id.
Search Song /playlist/<int:playlist_id>/search?search={search}&property={property} - Search for matching song within playlist at playlist_id, using search parameters search (the search term) and property (the song attribute to search).

