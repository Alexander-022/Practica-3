from app import db
import uuid
##from models.typestatus import TypeStatus

class DetalleFactura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(100))
    cantidad = db.Column(db.String(100))
    
    
   
    #civilstatus = db.Column(db.Enum(TypeStatus))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    factura_id = db.Column(db.Integer, db.ForeignKey('factura.id'), unique=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    #account = db.relationship('Account', backref='person', lazy=True)

    @property
    def serialize(self):
        return {
            'descripcion': self.descripcion,
            'cantidad': self.cantidad,
           
            'external_id': self.external_id,
        } 