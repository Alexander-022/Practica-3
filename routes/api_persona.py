from flask import Blueprint, jsonify, make_response, request
from controllers.personaController import PersonaController
from controllers.utilities.errors import Errors
from flask_expects_json import expects_json
#from controllers.autheticate import token_requeird

api_persona = Blueprint("api_persona", __name__)

personC = PersonaController()


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "lastname": {"type": "string"},
        "age": {"type": "string"},
        "status": {"type": "string"},
        "rol_id": {"type": "integer"},
    },
    "required": ["name", "lastname", "age", "status"],
}
schema_persona = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "apellido": {"type": "string"},
        "direccion": {"type": "string"},
        "cedula": {"type": "string"},
        "correo": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        },
        "clave": {"type": "string"},
        "persona_id": {"type": "string"},
    },
    "required": ["nombre", "apellido", "direccion", "cedula", "correo", "clave", "persona_id"],
}
schema_session = {
    "type": "object",
    "properties": {
        "correo": {"type": "string"},
        "clave": {"type": "string"},
    },
    "required": ["correo", "clave"],
}


# API for person


@api_persona.route("/person/<external>", methods=["GET"])
def search_external(external):
    search = personC.search_external(external)
    if search is None:
        return make_response(jsonify({"msg": "Person not found", "code": "404"}), 404)
    else:
        return make_response(
            jsonify({"msg": "OK", "code": "200", "data": search.serialize}), 200
        )


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


@api_persona.route('/persona', methods=["GET"])
def list():
    census = personC.listPersona()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([i.serialize for i in personC.listPersona()])}),
        200
    )

@api_persona.route("/persona/save", methods=["POST"])
@expects_json(schema_persona)
def create():
    data = request.json
    persona_id = personC.guardar_persona(data)
    if persona_id >= 0:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "data": "saved data"}), 200
        )
    else:
        return make_response(
            jsonify(
                {"msg": "ERROR", "code": 400, "data": {"error": Errors.error["-2"]}}
            ),
            400,
        )


@api_persona.route("/modify_person", methods=["POST"])
def modify_person():
    data = request.json
    modified_person = personC.modify_person(data)
    if modified_person == -3:
        return make_response(
            jsonify(
                {"msg": "ERROR", "code": 400, "error": Errors.person_not_found["-3"]}
            ),
            400,
        )
    else:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "data": {"person_saved": "saved data"}}),
            200,
        )


@api_persona.route("/deactivate_person/<external_id>", methods=["GET"])
def delete_person(external_id):
    success = personC.desactivate_account(external_id)
    if success:
        return make_response(
            jsonify(
                {"msg": "OK", "code": 200, "data": {"account": "Deactivated account"}}
            ),
            200,
        )
    else:
        return make_response(
            jsonify(
                {
                    "msg": "ERROR",
                    "code": 400,
                    "error": "The person with the external_id does not exist",
                }
            ),
            404,
        )




@api_persona.route("/session", methods=["POST"])
@expects_json(schema_session)
def session():
    data = request.json
    id = personC.login(data)
    if (type(id)) == int:
        return make_response(
            jsonify(
                {"msg": "ERROR", "code": 400, "datos": {"error": Errors.error.get(str(id))}}
            ),
            400,
        )
    else:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos":id }), 200
        )
