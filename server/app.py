#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'




# Flask application in flask_app.py has a resource available at "/bakeries"
@app.route('/bakeries')
def bakeries():
    # strategy for serialization
    bakeries = Bakery.query.all()
    bakeries_serialized = [bakery.to_dict() for bakery in bakeries]
    # Flask application in flask_app.py returns JSON representing models.Bakery objects.
    response = make_response(
        jsonify(bakeries_serialized),
        200
    )
    # Flask application in flask_app.py provides a response content type of application/json at "/bakeries"
    response.headers['Content-Type'] = 'application/json'
    return response

# Flask application in flask_app.py has a resource available at "/bakeries/<int:id>
@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    # strategy for serialization
    bakery = Bakery.query.filter_by(id=id).first()
    bakery_dict = bakery.to_dict()
    # Flask application in flask_app.py returns JSON representing one models.Bakery object
    response = make_response(
        jsonify(bakery_dict),
        200
    )
    # Flask application in flask_app.py provides a response content type of application/json at "/bakeries/<int:id>"
    response.headers['Content-Type'] = 'application/json'
    return response




# Flask application in flask_app.py has a resource available at "/baked_goods/by_price"
@app.route('/baked_goods/by_price')
def baked_goods_by_price():

    baked_goods_by_price = BakedGood.query.order_by(BakedGood.price).all()
    baked_goods_by_price_dict = [
        baked_good.to_dict() for baked_good in baked_goods_by_price
    ]
    # Flask application in flask_app.py returns JSON representing one models.Bakery object.
    response = make_response(
        jsonify(baked_goods_by_price_dict),
        200
    )
    # Flask application in flask_app.py provides a response content type of application/json at "/baked_goods/by_price" 
    response.headers['Content-Type'] = 'application/json'
    return response




# Flask application in flask_app.py has a resource available at "/baked_goods/most_expensive".
@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():

    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).limit(1).first()
    most_expensive_dict = most_expensive.to_dict()
    # Flask application in flask_app.py returns JSON representing one models.BakedGood object
    response = make_response(
        jsonify(most_expensive_dict),
        200
    )
    # Flask application in flask_app.py provides a response content type of application/json at "/bakeries/<int:id>" 
    response.headers['Content-Type'] = 'application/json'
    return response





if __name__ == '__main__':
    app.run(port=5555, debug=True)
