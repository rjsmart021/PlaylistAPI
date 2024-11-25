from flask import jsonify, request

from Playlist import app
from Playlist.models import Songs
from Playlist import db
from Playlist.schemas import SongsSchema

Songs_schema = SongsSchema()

@app.route('/songs', methods=['POST'])
def add_Songs():
    """
    Add Songs . Example POST data format
    {
    "Songs_name": "abc",
    "Artst_name": "abc",
    :Genre": "abd"
    }
    :return: success or error message
    """
    try:
        data = request.get_json()
        errors = Songs_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        Artist_name = data.get("Artist_name")
        Genre = data.get("Genre")
        # Check if the Songs already exists based on Artist_name or Record_lable
        existing_Songs = Songs.query.filter(
            (Songs.Artist_name == Artist_name) | (Songs.Genre == Genre)
        ).first()

        if existing_Songs:
            return jsonify({"message": f"Songs already existed"})
        Song = Song(Song_name=data["Song_name"], Artist_name=data["Artist_name"],
                            Genre=data["Genre"])

        # Add the new customer to the database
        db.session.add(Songs)
        db.session.commit()

        return jsonify({"message": "Songs added successfully"})
    except Exception as e:
        return jsonify({"Error": f"Songs not added. Error {e}"})


@app.route('/Songs/<int:Song_id>', methods=['GET'])
def get_Song(Song_id):
    """
    Get Songs data based on ID provided
    :param Songs_id: ID of the registered Song.
    :return: Song details oif found else Error message
    """
    try:
        Song = Songs.query.get(Songs_id)

        if Songs:
            Songs_data = {
                "Songs_id": Songs.Songs_id,
                "Songs_name": Songs.Songs_name,
                "Artist": Artist.Artist_Name,
                "Record_lable": Songs.Record_lable
            }
            return jsonify(Songs_data)
        else:
            return jsonify({"message": "Songs not found"})

    except Exception as e:
        print(f"Error in getting Songs. Error Message: {e}")
        return jsonify(
            {"message": f"Error while fetching Songs with ID: {Songs_id}. Error: {e}"})


@app.route('/Songs/<int:Songs_id>', methods=['PUT'])
def update_user(Songs_id):
    """
    Update the Songs details.
    example PUT data to update;
    {
    "Songs_name": "name",
    "Artist": "Artist_Name",
    "Genre": "Genre_Name"
    }
    :param Songs_id:
    :return:
    """
    try:
        Songs = Songs.query.get(Songs_id)

        if Songs:
            data = request.get_json()
            error = Songs_schema.validate(data)
            if error:
                return jsonify(error), 400
            Songs.Songs_name = data.get('Songs_name', Songs.Songs_name)
            Songs.Artist_Name = data.get('Artist', Artist.Artist_Name)
            Songs.Genre = data.get('phone_number', Genre.Genre_Name)

            db.session.commit()
            return jsonify({"message": "Songs updated successfully"})
        else:
            return jsonify({"message": "Songs Not Found!!!"})
    except Exception as e:
        return jsonify({"message": f"error in updating Songs. Error: {e}"})


@app.route('/Songs/<int:Songs_id>', methods=['DELETE'])
def delete_user(Songs_id):
    """
    Delete user based on the ID provided
    :param Songs_id: ID of the Songs to delete
    :return: success message if user deleted successfully else None
    """

    try:
        Songs = Songs.query.get(Songs_id)

        if Songs:
            # Delete the Songs from the database
            db.session.delete(Songs)
            db.session.commit()
            return jsonify({"message": "Songs deleted successfully"})
        else:
            return jsonify({"message": "Songs not found"})

    except Exception as e:
        return jsonify({"message": f"error in deleting Songs. Error: {e}"})
