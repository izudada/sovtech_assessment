from flask import jsonify, make_response, request
import datetime
from api import app, db, Users
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt


def resolve_create_user(obj, info, name, password):
    try:
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = Users(
                            public_id=str(uuid.uuid4()), 
                            name=name, 
                            password=hashed_password, 
                            admin=False
                        )
        db.session.add(new_user) 
        db.session.commit()  
        payload = {
            "success": True,
            "user": new_user.to_dict()
        }
    except ValueError:  
        payload = {
            "success": False,
            "errors": "Issue creating user"
        }

    return payload

def resolve_login_user(obj, info, username, password):
    try:
        user = Users.query.filter_by(name=username).first()  
        if check_password_hash(user.password, password):
            user_token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=7200)}, app.config['SECRET_KEY'], "HS256")
            token_data = {
                "name": username,
                "token": user_token
            }
            payload = {
                "success": True,
                "token": token_data
            }

    except ValueError:  
        payload = {
            "success": False,
            "errors": "login required"
        }

    return payload
    