from app import db

class Pharmacy(db.Model):
    #format: pharmacy name, address, city, state, zip, latitude, longitude
    id = db.Column(db.Integer, primary_key=True)
    pharmacy_name = db.Column(db.String(64))
    address = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zip = db.Column(db.String(64))
    latitude = db.Column(db.String(64), index=True)
    longitude = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Pharmacy {}>'.format(self.pharmacy_name)