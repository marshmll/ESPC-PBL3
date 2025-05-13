from models.db import db
from models.iot.devices import Device

class Actuator(db.Model):
    __tablename__ = 'actuator'
    id = db.Column('id', db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey(Device.id))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    @staticmethod
    def save_actuator(name, brand, model, topic, unit, is_active):
        device = Device(name=name, brand=brand, model=model, is_active=is_active)
        actuator = Actuator(device_id=device.id, unit=unit, topic=topic)

        device.actuators.append(actuator)
        db.session.add(device)
        db.session.commit()

    @staticmethod
    def get_actuators():
        actuators = Actuator.query.join(Device, Device.id == Actuator.device_id).add_columns(
            Device.id,
            Device.name,
            Device.brand,
            Device.model,
            Device.is_active,
            Actuator.topic,
            Actuator.unit
        ).all()

        return actuators

    @staticmethod
    def get_single_actuator(id):
        actuator = Actuator.query.filter(Actuator.device_id == id).first()
        if actuator is not None:
            actuator = Actuator.query.filter(Actuator.device_id == id).join(Device).add_columns(
                Device.id,
                Device.name,
                Device.brand,
                Device.model,
                Device.is_active,
                Actuator.topic,
                Actuator.unit
            ).first()

        return [actuator]
    
    def update_actuator(id,name, brand, model, topic, unit, is_active):
        device = Device.query.filter(Device.id == id).first()
        actuator = Actuator.query.filter(Actuator.device_id == id).first()
        if device is not None:
            device.name = name
            device.brand = brand
            device.model = model
            actuator.topic = topic
            actuator.unit = unit
            device.is_active = is_active
            db.session.commit()
        
        return Actuator.get_actuators()
    
    @staticmethod
    def delete_actuator(id):
        device = Device.query.filter(Device.id == id).first()
        actuactor = Actuator.query.filter(Actuator.device_id == id).first()
        db.session.delete(actuactor)
        db.session.delete(device)
        db.session.commit()
        return Actuator.get_actuators()