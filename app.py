from flask import Flask 
from flask_restful import Api

from common.database.db import initialize_db
from common.util.marshal import initialize_marshal

from controllers import TrackController
from controllers import PlaylistController
from controllers import PlaylistTrackController

app = Flask(__name__) 
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PlaylistManagementDB.db' 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

initialize_db(app)
initialize_marshal(app)

api.add_resource(TrackController.TrackController, '/api/tracks')
api.add_resource(PlaylistController.PlaylistController, '/api/playlists')
api.add_resource(PlaylistTrackController.PlaylistTrackController, '/api/playlisttracks')

if __name__ == '__main__':
    app.run(debug=True)

     
