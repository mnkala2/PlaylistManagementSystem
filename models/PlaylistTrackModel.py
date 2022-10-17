from common.database.db import db


class PlaylistTrack(db.Model):
    playlisttrack_id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer)
    track_id = db.Column(db.Integer)

    def __init__(self, playlist_id, track_id):
        self.playlist_id = playlist_id
        self.track_id = track_id      
 