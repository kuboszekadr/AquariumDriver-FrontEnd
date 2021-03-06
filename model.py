from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql

db = SQLAlchemy()


class Measure(db.Model):
    __tablename__ = "d_measure"
    measure_id = db.Column(db.Integer(), primary_key=True)
    measure_name = db.Column(db.String(255))


class Sensor(db.Model):
    __tablename__ = "d_sensor"
    sensor_id = db.Column(db.Integer(), primary_key=True)
    sensor_name = db.Column(db.String(255))


class DeviceSensor(db.Model):
    __tablename = "device_sensor"

    device_id = db.Column(db.Integer(), primary_key=True)
    device_name = db.Column(db.String())
    sensor_id = db.Column(db.Integer(), primary_key=True)
    sensor_name = db.Column(db.String())
    sensor_label = db.Column(db.String())
    measure_id = db.Column(postgresql.ARRAY(db.Integer()))


class Reading(db.Model):
    __tablename__ = 'reading'

    reading_id = db.Column(db.Integer(),
                           db.Sequence('reading_reading_id_seq'),
                           primary_key=True)
    sensor_id = db.Column(db.Integer())
    device_id = db.Column(db.Integer())

    reading_value = db.Column(db.Numeric())
    measure_id = db.Column(db.Integer())
    reading_timestamp = db.Column(db.DateTime())


class ProgramRuntime(db.Model):
    __tablename__ = 'program_runtime'

    id = db.Column(db.Integer(),
                   db.Sequence('program_runtime_id_seq'),
                   primary_key=True)

    program_id = db.Column(db.Integer())

    execution_id = db.Column(db.Integer())
    execution_timestamp = db.Column(db.DateTime())

    step = db.Column(db.Integer())
    is_active = db.Column(db.Boolean())


class FrondEndReading(db.Model):
    __tablename__ = 'reading'
    db.Model.metadata.schema = 'front_end'

    device_id = db.Column(db.Integer(), primary_key=True)

    sensor_id = db.Column(db.Integer(), primary_key=True)
    sensor_label = db.Column(db.Integer(), primary_key=True)

    measure_id = db.Column(db.Integer(), primary_key=True)
    measure_name = db.Column(db.String())

    reading_value = db.Column(db.Numeric())
    reading_count = db.Column(db.Integer())
    reading_timestamp_label = db.Column(db.String(), primary_key=True)
