from flask import Blueprint, jsonify, make_response, request
from flask import Flask, request, jsonify, make_response
from controllers.loteproductoControllers import LoteProductoController
from controllers.utilities.errors import Errors
from flask_expects_json import expects_json
from flask import Flask

import logging

from werkzeug.utils import secure_filename
import os


from controllers.authenticate import token_require

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB, ajusta según tus necesidades

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


api_loteproducto = Blueprint("api_loteproducto", __name__)

lproductoC = LoteProductoController()


schema = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "fecha_fab": {"type": "string"},
        "fecha_ven": {"type": "string"},
        "cantidad": {"type": "string"},
        "estado": {
            "type": "string",
            "enum": ["Bueno", "Al_caducar", "Caducado", "No_disponible"]
        },
        "descripcion": {"type": "string"},
        "nombre_sucursal": {"type": "string"},
        "longitud": {"type": "string"},
        "latitud": {"type": "string"},
    },
    "required": ["nombre", "fecha_fab", "fecha_ven", "cantidad", "estado", "descripcion", "nombre_sucursal", "longitud", "latitud"]
}

schema_up = {
    "type": "object",
    "properties": {
        "imagen_url": {"type": "string"}
    },
    "required": ["imagen_url"]
}

 





@api_loteproducto.route('/lproducto', methods=["GET"])
def list():
    census = lproductoC.listLoteProducto()
    serialized_data = [i.serialize for i in lproductoC.listLoteProducto()]
    # Convertir el atributo 'estado' a cadena en cada objeto serializado
    for data in serialized_data:
        data['estado'] = str(data['estado'])
    return make_response(
        
        jsonify({"msg":"OK", "code":200, "datos": serialized_data}),
        200
    )

@api_loteproducto.route('/lproducto/bueno', methods=["GET"])
def listarPnoCadu():
    census = lproductoC.listar_productos_no_caducados()
    serialized_data = [i.serialize for i in lproductoC.listar_productos_no_caducados()]
    # Convertir el atributo 'estado' a cadena en cada objeto serializado
    for data in serialized_data:
        data['estado'] = str(data['estado'])
    return make_response(
        jsonify({"msg":"OK", "code":200, "data": serialized_data}),
        200
    )

@api_loteproducto.route('/lproducto/al/caducar', methods=["GET"])
def listarPalCadu():
    census = lproductoC.listar_productos_proximos_caducar()
    serialized_data = [i.serialize for i in lproductoC.listar_productos_proximos_caducar()]
    # Convertir el atributo 'estado' a cadena en cada objeto serializado
    for data in serialized_data:
        data['estado'] = str(data['estado'])
    return make_response(
        jsonify({"msg":"OK", "code":200, "data": serialized_data}),
        200
    )

@api_loteproducto.route('/lproducto/caducado', methods=["GET"])
def listarPCaducados():
    census = lproductoC.listar_productos_caducados()
    serialized_data = [i.serialize for i in lproductoC.listar_productos_caducados()]
    # Convertir el atributo 'estado' a cadena en cada objeto serializado
    for data in serialized_data:
        data['estado'] = str(data['estado'])
    return make_response(
        jsonify({"msg":"OK", "code":200, "data": serialized_data}),
        200
    )

@api_loteproducto.route('/lproducto/dadodebaja', methods=["GET"])
def listarPsinStock():
    census = lproductoC.actualizar_estado_productos_caducados()
    serialized_data = [i.serialize for i in lproductoC.actualizar_estado_productos_caducados()]
    # Convertir el atributo 'estado' a cadena en cada objeto serializado
    for data in serialized_data:
        data['estado'] = str(data['estado'])
    return make_response(
        jsonify({"msg":"OK", "code":200, "data": serialized_data}),
        200
    )

@api_loteproducto.route("/loteproducto/save", methods=["POST"])
#@token_require 
@expects_json(schema)  
def create():
    try:
        data = request.json
        print('Datos recibidos en el backend:', data) 

        # Llamar al método para guardar el LoteProducto
        lproducto = lproductoC.guardar_LoteProducto(data)

        if lproducto:
            return jsonify({"msg": "OK", "code": 200, "data": "Datos guardados correctamente"}), 200
        else:
            return jsonify({"msg": "ERROR", "code": 400, "data": {"error": "No se pudo guardar el producto"}}), 400

    except Exception as e:
        return jsonify({"msg": "ERROR", "code": 500, "data": {"error": str(e)}}), 500

    
@app.route("/update/image", methods=["POST"])
@expects_json(schema_up)  
def updateimg():
    try:
        if 'file' not in request.files:
            return make_response(
                jsonify({"msg": "ERROR", "code": 400, "data": {"error": "No se proporcionó ninguna imagen"}}),
                400,
            )

        image_file = request.files['file']

        if image_file.filename == '':
            return make_response(
                jsonify({"msg": "ERROR", "code": 400, "data": {"error": "Nombre de archivo no válido"}}),
                400,
            )

        # Guarda la imagen en tu sistema de archivos
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(image_path)

        # Devuelve una respuesta exitosa
        return jsonify({"msg": "OK", "code": 200, "data": {"url": f"/{UPLOAD_FOLDER}/{filename}"}}), 200

    except Exception as e:
        return make_response(
            jsonify({"msg": "ERROR", "code": 500, "data": {"error": str(e)}}),
            500,
        )



#@api_loteproducto.route("/loteproducto/save", methods=["POST"])
#@token_require
#@expects_json(schema)
#def create():
#    data = request.json
#    lproducto = lproductoC.guardar_LoteProducto(data)
#    if lproducto:
#        return make_response(
#            jsonify({"msg": "OK", "code": 200, "data": {"tag": "saved data"}}), 200
#        )
#    else:
#        return make_response(
#            jsonify(
#                {"msg": "ERROR", "code": 400, "data": {"error": Errors.error["-2"]}}
#            ),
#            400,
#        )



