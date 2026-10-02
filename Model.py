from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Product(BaseModel):
    Id:int
    Name:str
    Price:float
    Quantity:float

product_list=[
    Product(Id=1,Name='Balu',Price=5.99,Quantity=10),
    Product(Id=2,Name='Sai',Price=6.99,Quantity=20),
    Product(Id=3,Name='Mahesh',Price=7.99,Quantity=40),
    Product(Id=4,Name='Kali',Price=8.99,Quantity=60),
    Product(Id=5,Name='Malik',Price=20.99,Quantity=100),
    Product(Id=6,Name='Kosh',Price=22.99,Quantity=200),

]

###To get the data mens retrive the data from server
@app.get('/products')
def get_products():
    return product_list

####To put the data meand update/replace the data
@app.put('/products/{Product_Id}')
def update_products(Product_Id:int,Updated_product:Product):
    for index, prod in enumerate(product_list):
        if prod.Id==Product_Id:
            product_list[index]=Updated_product
            return {'Product Updated':Updated_product}
    return {'Product Not Found'}



####To delect or drop the in data
@app.delete('/products/{Product_Id}')
def delete_products(Product_Id:int):
    for index, prod in enumerate(product_list):
        if prod.Id==Product_Id:
            delete=product_list.pop(index)
            return {'Product Deleted':delete}
    return {'Product Not Found'}


