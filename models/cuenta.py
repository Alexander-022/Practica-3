from app import db
import uuid

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    correo = db.Column(db.String(150), unique=True)
   
    clave = db.Column(db.String(250))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False, unique=True)
    
    # def copy(self, value):
    
    @property
    def serialize(self):
        return {
            'correo': self.correo,
           
            'external_id': self.external_id,
        } 
        
    def getPerson(self, id_p):
        print("Recibir: ", id_p)
        from models.persona import Persona
        return Persona.query.filter_by(id=id_p).first()
    