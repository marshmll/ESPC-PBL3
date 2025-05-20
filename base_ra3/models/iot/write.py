from models.db import db
from models.iot.sensors import Sensor
from models.iot.devices import Device
from datetime import datetime

class Write(db.Model):
    __tablename__ = 'write'
    id= db.Column('id', db.Integer, nullable = False, primary_key=True)
    write_datetime = db.Column(db.DateTime(), nullable = False)
    sensor_id= db.Column(db.Integer, db.ForeignKey(Sensor.id), nullable = False)
    value = db.Column( db.Float, nullable = True)

    @staticmethod
    def save_write(topic, value):
        sensor = Sensor.query.filter_by(topic=topic).first()
        device = Device.query.filter(Device.id == sensor.device_id).first()
        if (sensor is not None) and (device.is_active==True):
            write = Write(write_datetime = datetime.now(), sensor_id = sensor.id, value = float(value) )
            db.session.add(write)
            db.session.commit()

    @staticmethod
    def get_write(device_id, start, end):
        sensor = Sensor.query.filter_by(device_id=device_id).first()
        write = Write.query.filter(Write.sensor_id == sensor.id,
            Write.write_datetime > start,
            Write.write_datetime<end).all()
        return write


