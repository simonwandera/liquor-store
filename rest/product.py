from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash, json

from .. import db

auth = Blueprint('product', __name__, url_prefix='/product')
import jwt 

