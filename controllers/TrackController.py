from flask import request, jsonify 
from flask_restful import Resource


from models import TrackModel

from common.database.db import db

from common.util.marshal import ma


class TrackSchema(ma.Schema):
    class Meta: 
        fields = ('track_id', 'title', 'track_format')

track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)

class TrackController(Resource):

    
    @staticmethod
    def get():
        try: track_id = request.args['track_id']
        except Exception as _: track_id = None

        if not track_id:
            tracks = TrackModel.Track.query.all()

      

            return jsonify(tracks_schema.dump(tracks))
        track = TrackModel.Track.query.get(track_id)
        return jsonify(track_schema.dump(track))

    @staticmethod
    def post():
        title = request.json['title']
        track_format = request.json['track_format']
      
        track = TrackModel.Track(title, track_format)
        db.session.add(track)
        db.session.commit()

        return jsonify(track_schema.dump(track))

    @staticmethod
    def put():
        try: track_id = request.args['track_id']
        except Exception as _: track_id = None
        if not track_id:
            return jsonify({ 'Message': 'Must provide the track ID' })
        track = Track.query.get(track_id)

        title = request.json['title']
        track_format = request.json['track_format']      

        track.title = title 
        track.track_format = track_format 
   
  

        db.session.commit()
        return jsonify({
            'Message': f'Track {title} altered.'
        })

    @staticmethod
    def delete():
        try: track_id = request.args['track_id']
        except Exception as _: track_id = None
        if not track_id:
            return jsonify({ 'Message': 'Must provide the Track ID' })
        track = Track.query.get(track_id)

        db.session.delete(track)
        db.session.commit()

        return jsonify({
            'Message': f'Track {str(track_id)} deleted.'
        })
