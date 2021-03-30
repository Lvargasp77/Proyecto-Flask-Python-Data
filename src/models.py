from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#class User(db.Model):
    #id = db.db.Column(db.Integer, primary_key=True)
    #email = db.db.Column(db.db.String(120), unique=True, nullable=False)
    #password = db.db.Column(db.db.String(80), unique=False, nullable=False)
    #is_active = db.db.Column(db.Boolean(), unique=False, nullable=False)

class UserFav(db.Model):
    __tablename__ = 'userfav'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(30))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(25))
    email = db.Column(db.String(30))
    #userfav = db.relationship(UserFav)

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(30))
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(30))
    gravity = db.Column(db.String(30))
    terrain = db.Column(db.String(30))
    population = db.Column(db.Integer)
    
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(30))
    skin_color = db.Column(db.String(30))
    eye_color = db.Column(db.String(30))
    birth_year = db.Column(db.String(30))
    gender = db.Column(db.String(30))

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(30))
    model = db.Column(db.Integer)
    passenger = db.Column(db.Integer)
    consumable = db.Column(db.String(30))
    starship_class = db.Column(db.String(30))
    lenght = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    hyperdrive_rating = db.Column(db.Integer)




    def to_dict(self):
        return {}