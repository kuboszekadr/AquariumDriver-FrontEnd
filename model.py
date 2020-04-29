from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Measure(db.Model):
    __tablename__ = 'd_measure'
    measure_id = db.Column(db.Integer(), primary_key=True)
    measire_name = db.Column(db.String(255))


class Sensor(db.Model):
    __tablename__ = 'd_sensor'
    sensor_id = db.Column(db.Integer(), primary_key=True)
    sensor_name = db.Column(db.String(255))    


class Reading(db.Model):
    __tablename__ = 'reading'
    
    reading_id = db.Column(db.Integer(), 
        db.Sequence('reading_reading_id_seq'), 
        primary_key=True)
    sensor_id = db.Column(db.Integer())

    reading_value = db.Column(db.Numeric())
    reading_measure = db.Column(db.Integer())
    reading_timestamp = db.Column(db.DateTime())    