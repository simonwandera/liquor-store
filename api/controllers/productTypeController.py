from api.model.models import Product, Product_type
from api import db

def insert(product_type):
    if (product_type.category_name == "" or product_type.category_name is None):
        raise Exception("Product name is required")
    if product_type.text_description == "" or product_type.text_description is None:
        raise Exception("Product description is required")

    db.session.add(product_type)
    db.session.commit()
    return True

def read(id):
    return 0

def update():
    return 0

def deleteById():
    return 0

def getAllProductsTypes():
    return Product_type.query.all()


def productTypeSerializer(productType):
    return{
        "category_name": productType.category_name,
        "text_description": productType.text_description,
        "image": productType.image
    }

