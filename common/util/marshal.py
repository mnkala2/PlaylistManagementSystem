

from flask_marshmallow import Marshmallow 

ma = Marshmallow()

def initialize_marshal(app):
    ma.init_app(app)

    

