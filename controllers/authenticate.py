from flask import Flask, request, jsonify, make_response, current_app
from flask_sqlalchemy import SQLAlchemy
import uuid
import jwt
from datetime import datetime, timedelta
from functools import wraps
from models.cuenta import Cuenta
from controllers.utilities.errors import Errors

#los token se envia por la cabezera y no por el cuerpo de la peticion ni parametros
def token_require(f):
    @wraps(f)
    def decored(*args, **kwargs):
        token = None
        if 'X-Access-Token' in request.headers:
            token = request.headers['X-Access-Token']
            
        if not token:
            return make_response(
                jsonify({"msg":"ERROR", "code":400, "data": {"error": Errors.error[str(-5)]}}),
                401
            )
        try:
            data = jwt.decode(token, algorithms="HS512", verify=True, key=current_app.config['SECRET_KEY'])
            user = Cuenta.query.filter_by(external_id = data["external_id"]).first()
            if not user:
                return make_response(
                    jsonify({"msg":"ERROR", "code":401, "data": {"error": Errors.error[str(-7)]}}),
                    401
                )
                
        except:
            return make_response(
                    jsonify({"msg":"ERROR", "code":401, "data": {"error": Errors.error[str(-7)]}}),
                    401
                )
        return f(*args, **kwargs)
    return decored