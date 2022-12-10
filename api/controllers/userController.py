from api.model.models import User
from flask import jsonify
from api import db

def insert(user):

    if (user.first_name == "" or user.first_name is None):
        raise Exception("First name is required")
    if user.other_names == "" or user.other_names is None:
        raise Exception("Last name are required")
    if user.gender == "" or user.gender is None:
        raise Exception("Gender is required")
    if user.dob == "" or user.dob is None:
        raise Exception("Date of birth is required")
    if user.email == "" or user.email is None:
        raise Exception("Email is required")
    if user.phone == "" or user.phone is None:
        raise Exception("Phone Number is required")
    if user.username == "" or user.username is None:
        raise Exception("Username is required")
    if user.password == "" or user.password is None:
        raise Exception("Password is required")
    if user.confirmPassword == "" or user.confirmPassword is None:
        raise Exception("Confirm Password is required")
    if(user.password != user.confirmPassword):
        raise Exception("Password mismatch")
    if checkUniqueUsername(user.username):
        raise Exception("Username already exists")

    db.session.add(user)
    db.session.commit()
    return True


def read(id):
    user = User.query.filter_by(id=id)
    if user.username:
        return user
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

def checkUniqueUsername(username):
    users = User.query.all()
    for user in users:
        if user.username == username:
            return True
    return False