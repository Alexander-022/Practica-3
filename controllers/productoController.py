
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

class ProductoController:
    def listProducto(self):
        return Producto.query.all()
    

    
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
        
    def guardar_Producto(self, data):

      
        producto = Producto()
        
        producto.nombre = data["nombre"]
        producto.precio = data["precio"]
        producto.cantidad = data["cantidad"]

        
       
        producto.external_id = uuid.uuid4()
        
       
        
        
        db.session.add(producto)
        db.session.commit()
        
        return producto
        
 
        
   