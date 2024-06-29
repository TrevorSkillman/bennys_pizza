"""
This file defines the database for benny's pizza app.
It includes two models: Category and MenuItem.
"""

from .extensions import db
# from sqlalchemy.dialects.postgresql import JSON

class Category(db.Model):
    """Represents a category in the menu, which can have subcategories."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # This is a relationship to allow categories to have subcategories
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    subcategories = db.relationship('Category', backref=db.backref('parent', lazy='dynamic'), remote_side=[id])


class MenuItem(db.Model):
    """Represents an item on the menu with details like price, sizes, and description."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=True)
    sizes = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='menu_items')

    def __repr__(self):
        """Provides a readable string of the MenuItem object."""
        return f'<MenuItem {self.name}>' # This is for a readable string representation of the object

    # Converting the model instance to a dictionary, which includes all fields
    def to_dict(self):
        """Converts the model instance to a dictionary including all fields."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'sizes': self.sizes,
            'description': self.description,
            'category_id': self.category_id
        }

    # adding a method to the MenuItem class to commit the changes made with prices and descriptions
    @classmethod
    def update_item(cls, item_id, description=None, price=None):
        """
        Updates the price and description of a menu item.
        
        Args:
            item_id (int): The id of the menu item to update.
            description (str): The new description for the item. which is optional.
            price (float): The new price for the item, which is optional.
        
        Returns:
            MenuItem: The updated menu item. Or None if the item is not found.
        """
        item = cls.query.get(item_id)
        if not item:
            return None
        
        if description is not None:
            item.description = description
        if price is not None:
            item.price = price

        db.session.commit()
        return item
        
