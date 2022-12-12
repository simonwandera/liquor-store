from api.model.models import Product
from api import db

def insert(product):

    if product.category_id == "" or product.category_id is None:
        raise Exception("Product description is required")
    if (product.name == "" or product.name is None):
        raise Exception("Product name is required")
    if product.text_description == "" or product.text_description is None:
        raise Exception("Text description is required")
    if (product.html_description == "" or product.html_description is None):
        raise Exception("html description is required")
    if product.buy_price == "" or product.buy_price is None:
        raise Exception("Buying price is required")
    if product.quantity_in_stock == "" or product.quantity_in_stock is None:
        raise Exception("Quantity in stock is required")

    db.session.add(product)
    db.session.commit()
    return True

def read(id):
    product = Product.query.filter_by(id=id)
    if product.name:
        return product
    else:
        raise Exception("Invalid product")

def update(product):
    try:
        db.session.update(product)
        db.session.commit()
        return True
    except:
        raise Exception("Invalid product id")

def deleteById(id):
    product = read(id)
    if product.name:
        db.session.delete(product)
        db.session.commit()
        return True
    else:
        raise Exception("Invalid product id")

def getAllProducts():
    return Product.query.all()

def productSerializer(product):
    return{
        "id": product.id,
        "name": product.name,
        "category_id": product.category_id,
        "text_description": product.text_description,
        "html_description": product.html_description,
        "buy_price": product.buy_price,
        "quantity_in_stock": product.quantity_in_stock,
        "image": product.image
    }