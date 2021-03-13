from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Product, Order, Password, Stock
import bcrypt


admin = Blueprint("admin", __name__, static_folder="admin_statics", template_folder="admin_templates")

@admin.route('/')
def adminHome():
    try: 
        user = Password.query.filter_by(gang=10).first()
        if bcrypt.checkpw(session['password'].encode('utf-8'), user.hashed):
            return render_template('admin.html')
        else:
            return redirect(url_for("admin.login"))
    except:
        return redirect(url_for("admin.login"))


@admin.route("/orders", methods=['GET', 'POST'])
def viewOrders():
    try:
        user = Password.query.filter_by(gang=10).first()
        if bcrypt.checkpw(session['password'].encode('utf-8'), user.hashed):
            return render_template("orders.html", values=Order.query.all())
        else:
            return redirect(url_for("admin.login"))
    except:
        return redirect(url_for("admin.login"))

@admin.route("/orderswitch", methods=['GET', 'POST'])
def switchOrder():
    if request.method == "POST":
        record = Order.query.filter_by(orderid=request.form.get('id', type=int)).first()
        print(request.form.get('id', type=int))
        if record.complete == 'complete':
            record.complete = 'incomplete'
        else:
            record.complete = 'complete'
        db.session.commit()

    return redirect(url_for('admin.viewOrders'))

@admin.route("/orderdelete", methods=['GET', 'POST'])
def deleteOrder():
    if request.method == "POST":
        record = Order.query.filter_by(orderid=request.form.get('id', type=int)).first()
        if record.complete == 'complete':
            record.complete = 'deleted'
        else:
            record.complete = 'complete'
        db.session.commit()

    return redirect(url_for('admin.viewOrders'))

@admin.route("/deletedOrders", methods=['GET', 'POST'])
def deletedOrders():
    return render_template("deleted.html", values=Order.query.all())

@admin.route("/addstock/<context>", methods=["POST", "GET"])
def addStock(context):
    # try:
    #     user = Password.query.filter_by(gang=10).first()
    #     if bcrypt.checkpw(session['password'].encode('utf-8'), user.hashed):
    product = Product.query.filter_by(name=context).first()
    print(product)
    if request.method == "POST":
        product = Product.query.filter_by(name=context).first()
        stock = Stock(request.form["size"], request.form["color"], request.form["price"], Product.query.filter_by(name=context).first())
        db.session.add(stock)
        db.session.commit()
    return render_template("addStock.html")
    #     else:
    #         return redirect(url_for("admin.login"))
    # except:
    #     return redirect(url_for("admin.login"))


@admin.route('/register', methods=['POST'])
def register():
    try:
        password = request.json.get('password', None)

        if not password:
            return 'Missing password', 400
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = Password(hashed)
        db.session.add(user)
        db.session.commit()

        return f'Worked', 200
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":

            user = Password.query.filter_by(gang=10).first()
            if bcrypt.checkpw(request.form.get("password").encode('utf-8'), user.hashed):
                session['password'] = request.form.get('password')
                flash('You have hacked into the mainframe')
                return redirect(url_for("admin.adminHome"))
            else:
                flash("Wrong password fucko")
    return render_template("login.html")
