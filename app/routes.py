from flask import Blueprint, render_template, jsonify
from .models import MenuItem, Category
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/menu/<category_name>')
def get_category(category_name):
    # Converting the category name to the title case 
    category_name = category_name.title()
    category = Category.query.filter_by(name=category_name).first()
    if not category:
        print("No category found for: ", category_name)
        return jsonify([]) # Return an empty list if the category is not found
    
    subcategories = Category.query.filter_by(parent_id=category.id).all()
    # Debugging print to check whats being returned
    print(f"Subcategories for {category_name}: {[{'id': cat.id, 'name': cat.name} for cat in subcategories]}")
    return jsonify([{'id': cat.id, 'name': cat.name} for cat in subcategories])

@main.route('/menu/items/<int:category_id>')
def items(category_id):
    try:
        items = MenuItem.query.filter_by(category_id=category_id).all()
        return jsonify([{
            'name': item.name,
            'price': item.price,
            'sizes': item.sizes if item.sizes else None
        } for item in items])
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


@main.route('/menu/starters') # Dynamic route
def starters():
    starter_category = Category.query.filter_by(name='Starters').first() 
    if not starter_category:
        return jsonify([]) # if starters category is not found, return an empty list.
    starter_categories = Category.query.filter_by(parent_id=starter_category.id).all()
    return jsonify([{'id': cat.id, 'name': cat.name} for cat in starter_categories])

@main.route('/menu/pizza')
def pizza():
    pizza_category = Category.query.filter_by(name='Pizza').first()
    if not pizza_category:
        return jsonify([])
    pizza_categories = Category.query.filter_by(parent_id=pizza_category.id).all()
    return jsonify([{'id': cat.id, 'name': cat.name} for cat in pizza_categories])

@main.route('/menu/subs')
def subs():
    subs_category = Category.query.filter_by(name='Subs').first()
    if not subs_category:
        return jsonify([])
    subs_categories = Category.query.filter_by(parent_id=subs_category.id).all()
    return jsonify([{'id': cat.id, 'name': cat.name} for cat in subs_categories])

@main.route('/menu/meals')
def meals():
    meals_category = Category.query.filter_by(name='Meals').first()
    if not meals_category:
        return jsonify([])
    meals_categories = Category.query.filter_by(parent_id=meals_category.id).all()
    return jsonify([{'id': cat.id, 'name': cat.name} for cat in meals_categories])

@main.route('/menu/strombolis')
def strombolis():
    strombolis_category = Category.query.filter_by(name='Strombolis').first()
    if not strombolis_category:
        return jsonify([])
    items = MenuItem.query.filter_by(category_id=strombolis_category.id).all()
    return jsonify([{'name': item.name, 'price': item.price, 'sizes': item.sizes if item.sizes else None} for item in items])

@main.route('/menu/desserts')
def desserts():
    # finding the desserts category
    desserts_category = Category.query.filter_by(name='Desserts').first()
    # if desserts category is not found, return an empty list
    if not desserts_category:
        return jsonify([])
    # finding all the items in the desserts category
    items = MenuItem.query.filter_by(category_id=desserts_category.id).all()
    return jsonify([{'name': item.name, 'price': item.price, 'sizes': item.sizes if item.sizes else None} for item in items])


@main.route('/menu/catering')
def catering():
    catering_category = Category.query.filter_by(name='Catering').first()
    if not catering_category:
        return jsonify([])
    items = MenuItem.query.filter_by(category_id=catering_category.id).all()
    return jsonify([{'name': item.name, 'price': item.price, 'sizes': item.sizes if item.sizes else None} for item in items])