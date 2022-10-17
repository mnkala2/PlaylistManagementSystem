from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

track_app = Flask(__name__) 

track_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PlaylistManagementDB.db' 

track_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(track_app) 


class Track(db.Model):
    track_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    track_format = db.Column(db.String(32))    

    def __init__(self, title, track_format):
        self.title = title
        self.track_format = track_format


    with track_app.app_context():
        db.create_all()

