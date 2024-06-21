from app import db
import uuid
##from models.typestatus import TypeStatus

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.String(100))
    cantidad = db.Column(db.String(100))
   
    
   
    #civilstatus = db.Column(db.Enum(TypeStatus))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    #account = db.relationship('Account', backref='person', lazy=True)


    @property
    def serialize(self):
        return {
          #  "status": 1 if self.status else 0,
            'nombre': self.nombre,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'external_id': self.external_id,
        }    