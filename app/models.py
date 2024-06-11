from .extensions import db
# from sqlalchemy.dialects.postgresql import JSON

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # This is a relationship to allow categories to have subcategories
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    subcategories = db.relationship('Category', backref=db.backref('parent', lazy='dynamic'), remote_side=[id])


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=True)
    sizes = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='menu_items')

def __repr__(self):
    return f'<MenuItem {self.name}>' # This is for a readable string representation of the object

# Converting the model instance to a dictionary, which includes all fields
def to_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'price': self.price,
        'sizes': self.sizes,
        'description': self.description,
        'category_id': self.category_id
    }