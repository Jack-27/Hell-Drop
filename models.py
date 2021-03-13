from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    _id = db.Column("id", db.Integer, primary_key =True)
    name = db.Column(db.String(64))
    descr = db.Column(db.Text, nullable=True)
    stocks = db.relationship('Stock', backref='product', lazy=True)


    def __init__(self, name, descr):
        self.name = name
        self.descr = descr


class Stock(db.Model):
    _id = db.Column("id", db.Integer, primary_key =True)
    size = db.Column(db.String(64))
    color = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


    def __init__(self, size, color, price, product):
        self.size = size
        self.color = color
        self.price = price
        self.product = product


class Order(db.Model):
    _id = db.Column("id", db.Integer, primary_key =True)
    productName = db.Column(db.String(64))
    customerName = db.Column(db.String(64))
    color = db.Column(db.String(64))
    address = db.Column(db.Text, nullable=True)
    quantity = db.Column(db.Float, nullable=False)
    complete = db.Column(db.String(64))
    orderid = db.Column(db.Integer, nullable=False)
    

    def __init__(self, productName, customerName, color, address, quantity, comp):
        self.address = address
        self.productName = productName
        self.quantity = quantity
        self.customerName = customerName
        self.color = color
        self.complete = comp
        self.orderid = len(Order.query.all()) + 1
        

class Password(db.Model):
    _id = db.Column("id", db.Integer, primary_key =True)
    hashed = db.Column(db.String(64))
    gang = db.Column(db.Integer)

    

    def __init__(self, hashed):
        self.hashed = hashed
        self.gang = 10

        
        