

from models.factura import Factura
from models.loteProducto import LoteProducto
from models.producto import Producto

from models.rol import Rol


from app import db

import uuid
import jwt
from datetime import datetime, timedelta
from flask import current_app

import uuid
import os
from flask import request, current_app
from werkzeug.utils import secure_filename 
from flask import jsonify
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'upload'


class LoteProductoController:
    def listLoteProducto(self):
        return LoteProducto.query.all()
    

    
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
        
    def guardar_LoteProducto(self, data):
        l_producto = LoteProducto()

        l_producto.nombre = data["nombre"]
        l_producto.fecha_fab = data["fecha_fab"]
        l_producto.fecha_ven = data["fecha_ven"]
        l_producto.cantidad = data["cantidad"]
        l_producto.estado = data["estado"]
        l_producto.descripcion = data["descripcion"]
        l_producto.nombre_sucursal = data["nombre_sucursal"]
        l_producto.longitud = data["longitud"]
        l_producto.latitud = data["latitud"]
        
        l_producto.external_id = uuid.uuid4()

        db.session.add(l_producto)
        db.session.commit()

        return l_producto

    
    def listar_productos_no_caducados(self):
        fecha_actual = datetime.now().date()
        return LoteProducto.query.filter(LoteProducto.fecha_ven > fecha_actual).all()
    
    def listar_productos_proximos_caducar(self):
        fecha_actual = datetime.now().date()
        fecha_prox_caducidad = fecha_actual + timedelta(days=5)
        return LoteProducto.query.filter(LoteProducto.fecha_ven > fecha_actual,
                                          LoteProducto.fecha_ven <= fecha_prox_caducidad).all()

    
    def listar_productos_caducados(self):
        fecha_actual = datetime.now().date()
        return LoteProducto.query.filter(LoteProducto.fecha_ven <= fecha_actual).all()
    
    def actualizar_estado_productos_caducados(self):
        # Calcula la fecha actual y la fecha límite para considerar productos próximos a caducar
        fecha_actual = datetime.now()
        fecha_limite = fecha_actual + timedelta(days=5)
        
        # Consulta los lotes de productos cuya fecha de vencimiento está dentro de los próximos 5 días
        lotes_caducar = LoteProducto.query.filter(LoteProducto.fecha_ven <= fecha_limite).all()
        
        # Itera sobre los lotes de productos obtenidos
        for lote in lotes_caducar:
            # Actualiza el estado del lote de producto a "Caducado"
            lote.estado = "Caducado"
        
        # Guarda los cambios en la base de datos
        db.session.commit()
        
        # Devuelve los lotes de productos actualizados
        return lotes_caducar
    


    
    @staticmethod
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @staticmethod
    def update_imagen(image_file):
        try:
            if not image_file:
                return {"msg": "ERROR", "code": 400, "data": {"error": "No se proporcionó ninguna imagen"}}, 400

            if image_file.filename == '' or '.' not in image_file.filename or image_file.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
                return {"msg": "ERROR", "code": 400, "data": {"error": "Tipo de archivo no permitido"}}, 400

            filename = secure_filename(image_file.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(image_path)

            imagen_url = f'/uploads/{filename}'  # Ajusta la URL según tu estructura de archivos y carpetas

            # Guardar la URL de la imagen en la base de datos
            product = LoteProducto(imagen_url=imagen_url)
            db.session.add(product)
            db.session.commit()

            return {"msg": "OK", "code": 200, "data": {"imagen_url": imagen_url}}, 200

        except Exception as e:
            db.session.rollback()
            return {"msg": "ERROR", "code": 500, "data": {"error": str(e)}}, 500


        
 
        
   