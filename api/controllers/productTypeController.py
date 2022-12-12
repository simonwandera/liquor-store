from api.model.models import Product, Product_type
from api import db

def insert(product_type):
    if (product_type.category_name == "" or product_type.category_name is None):
        raise Exception("category name is required")
    if product_type.text_description == "" or product_type.text_description is None:
        raise Exception("category description is required")

    db.session.add(product_type)
    db.session.commit()
    return True

def read(id):
    category = Product_type.query.filter_by(id=id).first()
    if category:
        return category
    else:
        raise Exception("Invalid category id")

def update(product_type):
    try:
        db.session.update(product_type)
        db.session.commit()
        return True
    except:
        raise Exception("Invalid product type id")

def deleteById(id):
    product_type = read(id)
    if product_type.category_name:
        db.session.delete(product_type)
        db.session.commit()
        return True
    else:
        raise Exception("Invalid product type id")

def getAllProductsTypes():
    return Product_type.query.all()


def productTypeSerializer(productType):
    return{
        "id": productType.id,
        "category_name": productType.category_name,
        "text_description": productType.text_description,
        "image": productType.image
    }

