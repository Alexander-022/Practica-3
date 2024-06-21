
from app import db
from copy import deepcopy
import uuid
##from models.typestatus import TypeStatus

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    cedula = db.Column(db.String(100))
    #civilstatus = db.Column(db.Enum(TypeStatus))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    account = db.relationship('Cuenta', backref='persona', lazy=True)

    
    @property
    def serialize(self):
        return {
          #  "status": 1 if self.status else 0,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'direccion': self.direccion,
            'cedula': self.cedula,
            'external_id': self.external_id,
        }    