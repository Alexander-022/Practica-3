from app import db
import uuid
from models.tipoEstado import TipoEstado

class LoteProducto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    fecha_fab = db.Column(db.Date)
    fecha_ven = db.Column(db.Date)
    cantidad = db.Column(db.String(100))
    estado = db.Column(db.Enum(TipoEstado))
    descripcion = db.Column(db.String(100))
    imagen_url = db.Column(db.String(120), nullable=True)
    
    #civilstatus = db.Column(db.Enum(TypeStatus))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    #account = db.relationship('Account', backref='person', lazy=True)
        
    @property
    def serialize(self):
        return {
            'fecha_fab': self.fecha_fab,
            'fecha_ven': self.fecha_ven,
            'cantidad': self.cantidad,
            'estado': self.estado,
            'descripcion': self.descripcion,
            'external_id': self.external_id,
        } 
    