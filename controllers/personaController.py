from models.persona import Persona
from models.cuenta import Cuenta
from models.detalleFactura import DetalleFactura
from models.factura import Factura
from models.loteProducto import LoteProducto
from models.producto import Producto

from models.rol import Rol


from app import db
import uuid
import jwt
from datetime import datetime, timedelta
from flask import current_app

class PersonaController:
    def listPersona(self):
        return Persona.query.all()
    

    
    # def save_censado(self,data):
    #     rol = Rol.query.filter_by(nombre="CENSADO").first()
    #     persona = Person()
    #     if rol:
    #         persona.external_id = uuid.uuid4()
    #         persona.apellido = data.get("apellido")
    #         persona.nombre = data.get("nombre")
    #         persona.estado_civil = data.get("estado_civil")
    #         persona.rol_id = rol.id
    #         db.session.add(persona)
    #         db.session.commit()
    #         return  persona.id
    #     else:
    #         return -1
        
    def guardar_persona(self, data):
        persona = Persona()
        
        persona.nombre = data["nombre"]
        persona.apellido = data["apellido"]
        persona.direccion = data["direccion"]
        persona.cedula = data["cedula"]
        persona.external_id = uuid.uuid4()
        
        # Guarda la persona en la base de datos
        db.session.add(persona)
        db.session.commit()
        
        # Crea una nueva cuenta y asigna el id de la persona
        cuenta = Cuenta()
        cuenta.correo = data["correo"] 
        cuenta.clave = data["clave"]  
        cuenta.external_id = uuid.uuid4()
        cuenta.persona_id = persona.id
        db.session.add(cuenta)
        db.session.commit()
        
        return cuenta.id
        
    
    def login(self, data):
        cuentaA = Cuenta.query.filter_by(correo=data["correo"]).first()
        if cuentaA:
        # Desencriptar contraseña
            if cuentaA.clave == data["clave"]:
                expire_time = datetime.now() + timedelta(minutes=30)
                token_payload = {
                    "external_id": cuentaA.external_id,
                    "expire": expire_time.strftime("%Y-%m-%d %H:%M:%S") 
                }
                print('-------------', token_payload)
                token = jwt.encode(
                    token_payload,
                    key=current_app.config["SECRET_KEY"],
                    algorithm="HS512"
                )    
                persona = cuentaA.persona
                user_info = {
                    "token": token,
                    "user": persona.apellido + " " + persona.nombre
                }
                return user_info
            else:
                return -6  
        else:
            return -6  

    
   
        
    def modificar_persona(self, data):
        persona = Persona.query.filter_by(external_id=data["external_id"]).first() #sql 
        if persona:
            if "nombre" in data:
                persona.nombre = data["nombre"]
            if "apellido" in data:
                persona.apellido = data["apellido"]
            
                
            new_external_id = str(uuid.uuid4())
            persona.external_id = new_external_id
            db.session.commit()
            modified_person = Persona(
                nombre=persona.nombre,
                apellido=persona.apelliido,
                
                external_id=new_external_id
            )
            return modified_person
        else:
            return -3
        

        
    def desactivate_account(self, external_id):
        person = Persona.query.filter_by(external_id=external_id).first()
        if person:
            for account in person.account:
                account.status = 'desactivo' 
            db.session.commit()
            return True
        else:
            return False
    
    