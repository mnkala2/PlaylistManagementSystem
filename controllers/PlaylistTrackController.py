from flask import request, jsonify 
from flask_restful import Resource


from models import PlaylistTrackModel

from common.database.db import db

from common.util.marshal import ma

class PlaylistTrackSchema(ma.Schema):
    class Meta: 
        fields = ('playlisttrack_id','playlist_id', 'track_id')

playlisttrack_schema = PlaylistTrackSchema()
playlisttracks_schema = PlaylistTrackSchema(many=True)

class PlaylistTrackController(Resource):
    @staticmethod
    def get():
        try: playlisttrack_id = request.args['playlisttrack_id']
        except Exception as _: playlisttrack_id = None

        if not playlisttrack_id:
            playlisttracks = PlaylistTrack.query.all()
            return jsonify(playlisttracks_schema.dump(playlisttracks))
        playlisttrack = PlaylistTrack.query.get(playlisttrack_id)
        return jsonify(playlisttrack_schema.dump(playlisttrack))

    @staticmethod
    def post():
        playlist_id = request.json['playlist_id']
        track_id = request.json['track_id']

        playlisttrack = PlaylistTrack(playlist_id, track_id)
        db.session.add(playlisttrack)
        db.session.commit()
        return jsonify({
            'Message': f'Playlist {playlist_id} inserted.'
        })

    @staticmethod
    def put():
        try: playlisttrack_id = request.args['playlisttrack_id']
        except Exception as _: playlisttrack_id = None
        if not playlisttrack_id:
            return jsonify({ 'Message': 'Must provide the playlist ID' })
        playlisttrack = PlaylistTrack.query.get(playlisttrack_id)

        playlist_id = request.json['playlist_id']
        track_id = request.json['track_id']
    
        playlisttrack.playlist_id = playlist_id
        playlisttrack.track_id = track_id 
   
  

        db.session.commit()
        return jsonify({
            'Message': f'Playlist {playlist_id} altered.'
        })

    @staticmethod
    def delete():
        try: playlisttrack_id = request.args['playlisttrack_id']
        except Exception as _: playlisttrack_id = None
        if not playlisttrack_id:
            return jsonify({ 'Message': 'Must provide the playlist ID' })
        playlisttrack = PlaylistTrack.query.get(playlisttrack_id)

        db.session.delete(playlisttrack)
        db.session.commit()

        return jsonify({
            'Message': f'Playlisttrack {str(playlisttrack_id)} deleted.'
        })
