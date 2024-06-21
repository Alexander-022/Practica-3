from flask import Blueprint, jsonify, make_response, request
from controllers.productoController import ProductoController
from controllers.utilities.errors import Errors
from flask_expects_json import expects_json
#from controllers.autheticate import token_requeird

api_producto = Blueprint("api_producto", __name__)

productoC = ProductoController()




schema = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "precio": {"type": "string"},
        "cantidad": {"type": "string"},
        
        
    },
    "required": ["nombre", "precio", "cantidad"],
}

schema_session = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["email", "password"],
}


# API for person





# @api_person.route('/person/save/censado', methods=["POST"])
# @expects_json(schema)
# def create():
#     data = request.json
#     person_id = personC.save_censado(data)
#     if(person_id >= 0):
#         return make_response(
#             jsonify({"msg":"OK", "code":200, "data": []}),
#             200
#         )
#     else:
#         return make_response(
#             jsonify({"msg":"ERROR", "code":400, "data": {"error": Errors.passwordrepeat[str(person_id)]}}),
#             400
#         )
# para modificar debo enviar el external, pero primero obtener el objeto, creaer metodo listar q=pero que retorne el objeto con el external id


@api_producto.route('/producto', methods=["GET"])
def list():
    census = productoC.listProducto()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([i.serialize for i in productoC.listProducto()])}),
        200
    )

@api_producto.route("/producto/save", methods=["POST"])
@expects_json(schema)
def create():
    data = request.json
    producto = productoC.guardar_Producto(data)
    if producto:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "data": {"tag": "saved data"}}), 200
        )
    else:
        return make_response(
            jsonify(
                {"msg": "ERROR", "code": 400, "data": {"error": Errors.error["-2"]}}
            ),
            400,
        )



