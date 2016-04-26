from app import db

class Listing(db.Model):
    __tablename__ = 'listing'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    week_number = db.Column(db.Integer)
    artist = db.Column(db.String)
    title = db.Column(db.String)
    spotify_url = db.Column(db.String)
    spotify_id = db.Column(db.String)
    image = db.Column(db.String)
