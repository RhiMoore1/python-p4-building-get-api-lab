from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
# We have two models, bakeries and baked goods, in a one-to-many relationship
db = SQLAlchemy(metadata=metadata)
# Update the Bakery and BakedGood models to set up the correct associations based on the structure of the tables.
# Use the relationship() SQLAlchemy method and SQLAlchemy-serializer's SerializerMixin class.
# Bakery model in models.py can be instantiated with a name
# Bakery model in models.py can create records that can be committed to the database.
# Bakery model in models.py can be used to retrieve records from the database.
# Bakery model in models.py can create records with a to_dict() method for serialization.
# Bakery model in models.py can delete its records.

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialize_rules = ('-baked_goods.bakery',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    baked_goods = db.relationship('BakedGood', backref='bakery')


# Update the Bakery and BakedGood models to set up the correct associations based on the structure of the tables.
# BakedGood model in models.py can be instantiated with a name and price.
# BakedGood model in models.py can create records that can be committed to the database.
# BakedGood model in models.py can be used to retrieve records from the database. 
# BakedGood model in models.py can create records with a to_dict() method for serialization.
# BakedGood model in models.py can delete its records.

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialize_rules = ('-bakery.baked_goods',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    