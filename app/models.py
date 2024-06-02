from .extensions import db
from sqlalchemy.dialects.postgresql import JSON

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # This is a relationship to allow categories to have subcategories
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    subcategories = db.relationship('Category', backref=db.backref('parent', lazy='dynamic'), remote_side=[id])


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # price = db.Column(db.Float, nullable=False)
    sizes = db.Column(JSON, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='menu_items')


