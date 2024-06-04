from .extensions import db
<<<<<<< HEAD
# from sqlalchemy.dialects.postgresql import JSON
=======
from sqlalchemy.dialects.postgresql import JSON
>>>>>>> f6e033f9f666e7ea67e374324f7c50bfb4b8aa25

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # This is a relationship to allow categories to have subcategories
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    subcategories = db.relationship('Category', backref=db.backref('parent', lazy='dynamic'), remote_side=[id])


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
<<<<<<< HEAD
    price = db.Column(db.Float, nullable=False)
    sizes = db.Column(db.String(200), nullable=True)
=======
    # price = db.Column(db.Float, nullable=False)
    sizes = db.Column(JSON, nullable=True)
>>>>>>> f6e033f9f666e7ea67e374324f7c50bfb4b8aa25
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='menu_items')