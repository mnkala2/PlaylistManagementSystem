from flask import request, jsonify 
from flask_restful import Resource


from models import PlaylistModel

from common.database.db import db

from common.util.marshal import ma

import logging

# Get logger
logger = logging.getLogger("Playlist Controller Logger")

# Create a handler
c_handler = logging.StreamHandler()

# link handler to logger
logger.addHandler(c_handler)

# Set logging level to the logger
logger.setLevel(logging.DEBUG) # <-- THIS!

class PlaylistSchema(ma.Schema):
    class Meta: 
        fields = ('playlist_id', 'name')

playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)

class PlaylistController(Resource):
    @staticmethod
    def get():
        logger.debug('Executing get playist') 

        try: playlist_id = request.args['playlist_id']
        except Exception as _: playlist_id = None

        if not playlist_id:
            playlists = PlaylistModel.Playlist.query.all()
            return jsonify(playlists_schema.dump(playlists))
        playlist = PlaylistModel.Playlist.query.get(playlist_id)
        return jsonify(playlist_schema.dump(playlist))

    @staticmethod
    def post():
        name = request.json['name']        

        playlist = PlaylistModel.Playlist(name)
        db.session.add(playlist)
        db.session.commit()

        return jsonify(track_schema.dump(playlist))

    @staticmethod
    def put():
        try: playlist_id = request.args['playlist_id']
        except Exception as _: playlist_id = None
        if not playlist_id:
            return jsonify({ 'Message': 'Must provide the playlist ID' })
        playlist = PlaylistModel.Playlist.query.get(playlist_id)

        name = request.json['name']
    
        playlist.name = name  
  
        db.session.commit()

        return jsonify(track_schema.dump(track))

    @staticmethod
    def delete():
        try: playlist_id = request.args['playlist_id']
        except Exception as _: playlist_id = None
        if not playlist_id:
            return jsonify({ 'Message': 'Must provide the playlist ID' })
        playlist = PlaylistModel.Playlist.query.get(playlist_id)

        db.session.delete(playlist)
        db.session.commit()

        return jsonify({
            'Message': f'Playlist {str(playlist_id)} deleted.'
        })