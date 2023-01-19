{
    "firstName": "simon",
    "lastName": "wandera",
    "gender":"male",
    
    "dob": "2000-4-4",
    "email": "simonwandera12@gmail.com",
    "phone":"+254713103666",
    "username": "simonwandera",
    "password": "12345678",
    "confirmPassword":"12345678"
  }

http://127.0.0.1:5000/user
user POST


-----------------


{
    "category_name": "Gin",
    "text_description": "This is a sample text description",
    "imageURL":"https://images/img.jpg"
  }


product type (Product category)
POST
https://liquorstorev1.pythonanywhere.com/product_type

-----------------------


{
    "category_id": 2,
    "name": "Red Label",
    "text_description":"You can use this gin or throw it away",
    "html_description": "Has always been my favourite taste",
    "buy_price": 4000,
    "quantity_in_stock":2000,
    "imageURL":"https://this.is.a.gpg"
  }

product
POST
----------------------------------


{
   "product_id": 1,
   "quantity":2
}


http://127.0.0.1:5000/productCart/add_to_cart
POST


-------------------

{
"product_id":"1"
}

http://127.0.0.1:5000/productCart/remove_from_cart

POST


http://127.0.0.1:5000/user/items_in_cart

GET
token required

-------------------------------------------

http://127.0.0.1:5000/user/cart
GET 
Token required
--------------------------------------------
http://127.0.0.1:5000/user/items_in_cart
token require

-------------------


http://127.0.0.1:5000/checkout


POST
token required








