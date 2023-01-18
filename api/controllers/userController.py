from api.model.models import User
from flask import jsonify
from api import db
from datetime import datetime
from dateutil import relativedelta
from werkzeug.security import generate_password_hash, check_password_hash


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
    if usernameExists(user.username):
        raise Exception("Username already exists")
    if emailExists(user.email):
        raise Exception("Email already exists")
    if not validAge(user.dob):
        raise Exception("You are not old enough to purchase alcohal")

    user.password = generate_password_hash(user.password, method='sha256')
    user.dob = datetime.strptime(user.dob, '%Y-%m-%d').date()
    user.gender = user.gender.upper()

    db.session.add(user)
    db.session.commit()
    return True


def read(id):
    user = User.query.filter_by(id=id).first()
    if user.username:
        return user
    else:
        raise Exception("Invalid user id")

# def getUserByUsername(username):
#     user = User.query.filter_by(username=username).first()
#     if user.username:
#         return user
#     else:
#         raise Exception("Invalid username")


def update(user):
    try:
        db.session.update(user)
        db.session.commit()
        return True
    except:
        raise Exception("Invalid category id")


def deleteById(id):
    user = read(id)
    if user.username:
        db.session.delete(user)
        db.session.commit()
        return True
    else:
        raise Exception("Invalid user id")


def getAllUsers():
    return User.query.all()


def userserializer(user):
    return {
        'id': user.id,
        'first_name': user.first_name,
        'other_names': user.other_names,
        'gender': user.gender,
        'dob': str(user.dob),
        'phone': user.phone,
        'username': user.username,
        'email': user.email,
        'usertype': user.usertype,
        'residence': user.residence,
        'pick_up_point': user.pick_up_point
    }

def usernameExists(username):
    users = User.query.all()
    for user in users:
        if user.username == username:
            return True
    return False

def emailExists(email):
    users = User.query.all()
    for user in users:
        if user.email == email:
            return True
    return False

def validAge(dob):
    dob = datetime.strptime(dob, '%Y-%m-%d').date()
    if relativedelta.relativedelta(datetime.now(), dob).years < 18:
        return False

    return True