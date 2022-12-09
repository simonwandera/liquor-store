from api.model.models import User
from flask import jsonify
from api import db

def insert(user):

    if (user.first_name == ""):
        raise Exception("First name is required")
    if user.other_names == "":
        raise Exception("Other names are required")
    if user.gender == "":
        raise Exception("Gender is required" )
    if user.dob == "":
        raise Exception("Date is required")
    if user.email == "":
        raise Exception("Email is required")
    if user.username == "":
        raise Exception("Username is required")
    if user.password == "":
        raise Exception("Password is required")
    
    db.session.add(user)
    db.session.commit()
    return True


def read(id):
    user = User.query.filter_by(id=id)
    if user.username:
        serialized_user = jsonify(userserializer(user))
        return serialized_user
    else:
        raise Exception("Invalid user id")

def update(user):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except:
        raise Exception("Invalid user id")


def deleteById(id):
    user = read(id)
    if user.username:
        db.session.delete(user)
        db.session.commit()
        return True
    else:
        raise Exception("Invalid user id")


def getAllUsers():
    users = User.query.all()
    all_users = jsonify([*map(userserializer, users)])
    return all_users


def userserializer(user):
    return {
        'id': user.id,
        'first_name': user.first_name,
        'other_names': user.other_names,
        'gender': user.gender,
        'dob': user.dob,
        'phone': user.phone,
        'username': user.username,
        'email': user.email,
        'usertype': user.usertype,
        'residence': user.residence,
        'pick_up_point': user.pick_up_point
    }