from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restful import Resource, Api




app = Flask(__name__) 
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PlaylistManagementDB.db' 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
ma = Marshmallow(app)


class Track(db.Model):
    track_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    track_format = db.Column(db.String(32))    

    def __init__(self, title, track_format):
        self.title = title
        self.track_format = track_format

class Playlist(db.Model):
    playlist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name
 
   
with app.app_context():
    db.create_all()

class TrackSchema(ma.Schema):
    class Meta: 
        fields = ('track_id', 'title', 'track_format')

track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)

class TrackManager(Resource):
    @staticmethod
    def get():
        try: track_id = request.args['track_id']
        except Exception as _: track_id = None

        if not track_id:
            tracks = Track.query.all()
            return jsonify(tracks_schema.dump(tracks))
        track = Track.query.get(track_id)
        return jsonify(track_schema.dump(track))

    @staticmethod
    def post():
        title = request.json['title']
        track_format = request.json['track_format']
      

        track = Track(title, track_format)
        db.session.add(track)
        db.session.commit()
        return jsonify({
            'Message': f'Track {title} inserted.'
        })

    @staticmethod
    def put():
        try: track_id = request.args['track_id']
        except Exception as _: track_id = None
        if not track_id:
            return jsonify({ 'Message': 'Must provide the user ID' })
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


class PlaylistSchema(ma.Schema):
    class Meta: 
        fields = ('playlist_id', 'name')

playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)

class PlaylistManager(Resource):
    @staticmethod
    def get():
        try: playlist_id = request.args['playlist_id']
        except Exception as _: playlist_id = None

        if not playlist_id:
            playlists = Playlist.query.all()
            return jsonify(playlists_schema.dump(playlists))
        playlist = Playlist.query.get(playlist_id)
        return jsonify(playlist_schema.dump(playlist))

    @staticmethod
    def post():
        name = request.json['name']
        

        playlist = Track(name)
        db.session.add(playlist)
        db.session.commit()
        return jsonify({
            'Message': f'Playlist {name} inserted.'
        })

    @staticmethod
    def put():
        try: playlist_id = request.args['playlist_id']
        except Exception as _: playlist_id = None
        if not playlist_id:
            return jsonify({ 'Message': 'Must provide the playlist ID' })
        playlist = Playlist.query.get(playlist_id)

        name = request.json['name']
    
        playlist.name = name 
   
  

        db.session.commit()
        return jsonify({
            'Message': f'Playlist {title} altered.'
        })

    @staticmethod
    def delete():
        try: playlist_id = request.args['playlist_id']
        except Exception as _: playlist_id = None
        if not playlist_id:
            return jsonify({ 'Message': 'Must provide the playlist ID' })
        playlist = Playlist.query.get(playlist_id)

        db.session.delete(playlist)
        db.session.commit()

        return jsonify({
            'Message': f'Playlist {str(playlist_id)} deleted.'
        })



api.add_resource(TrackManager, '/api/tracks')
api.add_resource(PlaylistManager, '/api/playlists')

if __name__ == '__main__':
    app.run(debug=True)

     