from flask import Blueprint, jsonify, make_response, request


# from models.rol import Rol
# from models.censu import Censu
#problem relations

# from models.personcensu import PersonCensu
# from models.motive import Catalogue
# from models.motivecensu import MotiveCensu
# from models.person import Person
api = Blueprint('api', __name__)

@api.route('/')
def home():
    return make_response(
        jsonify({"msg":"OK", "code":200}),
        200
    )
#API for person    
@api.route('/suma', methods=["POST"])
def suma_post():
    data = request.json
    print(data)
    #c= float(a) + float(b)
    c=0
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":{"suma":c}}),
        200
    )