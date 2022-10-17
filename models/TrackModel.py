
from common.database.db import db

class Track(db.Model):
    track_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    track_format = db.Column(db.String(32))    

    def __init__(self, title, track_format):
        self.title = title
        self.track_format = track_format

