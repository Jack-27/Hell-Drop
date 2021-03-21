from flask import Flask, render_template, url_for, redirect, request, session
from admin import admin
from flask_sqlalchemy import SQLAlchemy
from models import db, Product, Order, Stock
import os
#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, jsonify, request

import stripe
# This is your real test secret API key.
stripe.api_key = 'sk_test_51ITvrXCmOhKIxbevExOYKUZabF2kmdbfEiTKF5hnwjlVdB8QnEGxZxsmB97jPqiRFiMOnjBvkEqutrBpxHTUBtTG00GvSisBUG'

app = Flask(__name__,
            static_url_path='',
            static_folder='.')

YOUR_DOMAIN = 'http://localhost:4242'



app = Flask(__name__)
app.register_blueprint(admin, url_prefix= "/admin")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Product.db'
app.config['SECRET_KEY'] = 'ahdlohoifgheoif'
db.app = app
db.init_app(app)

@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/")
def redir():
    return redirect(url_for("home"))

@app.route("/gallery")
def gal():
    hists = os.listdir('static/gallery_pics')
    hists = ['gallery_pics/' + file for file in hists]
    return render_template('gallery.html', hists = hists)


@app.route("/shop")
def shopp():
    return render_template("shop.html", values=Product.query.all())

@app.route("/blab", methods=["POST", "GET"])
def blab():
    if request.method == "POST":
        ordr = Order(request.form['productName'],request.form['customerName'],request.form['color'], request.form['address'], request.form['quantity'], request.form['comp'])
        db.session.add(ordr)
        db.session.commit()
    return render_template("blab.html")

@app.route("/whitehell")
def whiteHell():
    hists = os.listdir('static/WhiteHell')
    hists = ['WhiteHell/' + file for file in hists]
    return render_template("whitehell.html", hists = hists)
    
@app.route("/bluehell")
def blueHell():
    hists = os.listdir('static/BlueHell')
    hists = ['BlueHell/' + file for file in hists]
    return render_template("bluehell.html", hists = hists)

@app.route("/pinkhell")
def pinkHell():
    hists = os.listdir('static/PinkHell')
    hists = ['PinkHell/' + file for file in hists]
    return render_template("pinkhell.html", hists = hists)

@app.route("/redhell")
def redHell():
    hists = os.listdir('static/RedHell')
    hists = ['RedHell/' + file for file in hists]
    return render_template("redhell.html", hists = hists)

@app.route('/processOrder', methods = ['GET', 'POST'])
def addOrder():
    req = request.json
    name = req["name"]
    address = req["address"]

    for d in range(0, len(session['cart'])):
        ordr = Order('hell', name, 'black', address, 1, 'incomplete')
        db.session.add(ordr)
        db.session.commit()
    session['cart'].clear()
    session.modified = True
    return ""

@app.route("/pleasedontactually")
def contact():
    return render_template("contactUs.html")

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403


@app.route("/drop", methods=["POST", "GET"])
def drop():
    if request.method == "POST": 
        db.session.commit()
        db.drop_all()
        db.create_all()
        return redirect(url_for("test"))
    return render_template("drop.html")

@app.route("/view_cart")
def cart():
    cart = session['cart'] 
    return render_template("viewCart.html", cart = cart)

@app.route('/clear')
def clear():
    session.clear()
    return "yuh"

if __name__ == "__main__":
    app.run(debug=True)
    with app.test_request_context():
        db.create_all()
