from flask_sqlalchemy import SQLAlchemy


# Initialize SQLAlchemy instance
# db = SQLAlchemy()
from . import db
# Base Product class with common fields
class Product(db.Model):
    __abstract__ = True  # This makes Product an abstract base class and it won't be mapped to a table
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)  # URL or file path
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    color = db.Column(db.String(15))
    rating = db.Column(db.Integer, default=0)
    category = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    sale = db.Column(db.Boolean, default=True)
    size_small = db.Column(db.Integer, default=0)
    size_medium = db.Column(db.Integer, default=0)
    size_large = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product {self.product_name} - {self.category}>"

# Inheriting the common Product fields in specific models
class Men(Product):
    __tablename__ = 'men'

class Women(Product):
    __tablename__ = 'women'

class Kids(Product):
    __tablename__ = 'kids'

class Accessories(Product):
    __tablename__ = 'accessories'

class Shoes(Product):
    __tablename__ = 'shoes'