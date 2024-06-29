"""
Defining the routes for the application
It includes routes for the main page, admin functions, and menu sections.
"""
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from .models import MenuItem, Category
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Rednering the home page."""
    return render_template('index.html')

# ADMIN ROUTES #
@main.route('/admin', methods=['GET'])
def admin_page():
    """Rendering the admin page if the user is logged in; otherwise, redirect to login."""
    if 'username' in session:
        items = MenuItem.query.all() # fetching the items from the database
        return render_template('admin.html', items=items)
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    """Handle login requests. Authenticate the user and redirect to the admin page on successful login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'owner' and password == 'password123':
            session['username'] = username
            return redirect(url_for('main.admin_page'))
    return render_template('login.html')
    
@main.route('/logout')
def logout():
    """Log out the current user and redirect to the login page."""
    session.pop('username', None)
    return redirect(url_for('login'))

@main.route('/updatePricesAndDesc', methods=['POST'])
def update_prices_and_desc():
    """Where the admin changes item prices and desctriptions from the admin page."""
    data = request.get_json()
    item_id = data.get('itemId')
    item_desc = data.get('itemDesc')
    item_price = data.get('itemPrice')

    # Debugging print statements
    print(f"Item ID: {item_id}")
    print(f"Item Description: {item_desc}")
    print(f"Item Price: {item_price}")
    
    if not item_id:
        return jsonify({'message': 'Invalid input'}), 400

    # Ensuring at least one field is being updated of description or price
    if item_desc is None and item_price is None:
        return jsonify({'message': 'No Fields to update'}), 400
    
    updated_item = MenuItem.update_item(item_id, item_desc, item_price)
    if updated_item:
        return jsonify({'message': 'Update successful', 'item': updated_item.to_dict()}), 200
    else:
        return jsonify({'message': 'Update successful'}), 400
        


### MENU ROUTES ###
@main.route('/menu/<category_name>')
def get_category(category_name):
    """Return subcategories for the specified category.""" 
    category_name = category_name.title()
    category = Category.query.filter_by(name=category_name).first()
    if not category:
        print("No category found for: ", category_name)
        return jsonify([]) # Return an empty list if the category is not found
    
    subcategories = Category.query.filter_by(parent_id=category.id).all()
    # Debugging print to check whats being returned
    print(f"Subcategories for {category_name}: {[{'id': cat.id, 'name': cat.name} for cat in subcategories]}")
    return jsonify([{'id': cat.id, 'name': cat.name, 'image': f"images/{cat.name.lower()}_logo.png"} for cat in subcategories])

@main.route('/menu/items/<int:category_id>')
def items(category_id):
    """Return items for the specified category ID."""
    try:
        items = MenuItem.query.filter_by(category_id=category_id).all()
        category_name = Category.query.get(category_id).name
        return jsonify([{
            'name': item.name,
            'price': item.price,
            'sizes': item.sizes if item.sizes else None,
            'description': item.description,
            'category': category_name
        } for item in items])
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


@main.route('/menu/starters') # Dynamic route
def starters():
    """Return starter subcategories."""
    starter_category = Category.query.filter_by(name='Starters').first() 
    if not starter_category:
        return jsonify([]) # if starters category is not found, return an empty list.
    starter_categories = Category.query.filter_by(parent_id=starter_category.id).all()
    return jsonify([{'id': cat.id, 'name': cat.name, 'image': f"images/{cat.name.lower().replace(' ', '_')}_logo.png"} for cat in starter_categories])


@main.route('/menu/pizza')
def pizza():
    """Return pizza subcategories."""
    pizza_category = Category.query.filter_by(name='Pizza').first()
    if not pizza_category:
        return jsonify([])
    pizza_categories = Category.query.filter_by(parent_id=pizza_category.id).all()
    return jsonify([{'id': cat.id, 'name': cat.name, 'image': f"images/{cat.name.lower().replace(' ', '_')}_logo.png"} for cat in pizza_categories])

@main.route('/menu/subs')
def subs():
    """Returns subs subcategories."""
    subs_category = Category.query.filter_by(name='Subs').first()
    if not subs_category:
        return jsonify([])
    subs_categories = Category.query.filter_by(parent_id=subs_category.id).all()
    return jsonify([{'id': cat.id, 'name': cat.name, 'image': f"images/{cat.name.lower().replace(' ', '_')}_logo.png"} for cat in subs_categories])

@main.route('/menu/meals')
def meals():
    """Returns meals subcategories."""
    meals_category = Category.query.filter_by(name='Meals').first()
    if not meals_category:
        return jsonify([])
    meals_categories = Category.query.filter_by(parent_id=meals_category.id).all()
    return jsonify([{'id': cat.id, 'name': cat.name, 'image': f"images/{cat.name.lower().replace(' ', '_')}_logo.png"} for cat in meals_categories])

@main.route('/menu/strombolis')
def strombolis():
    """Return strombolis category items."""
    strombolis_category = Category.query.filter_by(name='Strombolis').first()
    if not strombolis_category:
        return jsonify([])
    items = MenuItem.query.filter_by(category_id=strombolis_category.id).all()
    return jsonify([{
        'name': item.name, 
        'price': item.price, 
        'sizes': item.sizes if item.sizes else None,
        'description': item.description
    } for item in items])

@main.route('/menu/desserts')
def desserts():
    """Return desserts category items."""
    desserts_category = Category.query.filter_by(name='Desserts').first()
    # if desserts category is not found, return an empty list
    if not desserts_category:
        return jsonify([])
    # finding all the items in the desserts category
    items = MenuItem.query.filter_by(category_id=desserts_category.id).all()
    return jsonify([{
        'name': item.name, 
        'price': item.price, 
        'sizes': item.sizes if item.sizes else None,
        'description': item.description    
    } for item in items])

@main.route('/menu/catering')
def catering():
    """Return catering category items."""
    catering_category = Category.query.filter_by(name='Catering').first()
    if not catering_category:
        return jsonify([])
    items = MenuItem.query.filter_by(category_id=catering_category.id).all()
    return jsonify([{
        'name': item.name, 
        'price': item.price, 
        'sizes': item.sizes if item.sizes else None,
        'description': item.description    
    } for item in items])

if __name__ == '__main__':
    from . import create_app
    app = create_app()
    app.run(debug=True)