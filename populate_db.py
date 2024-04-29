from app import create_app, db
from app.models import MenuItem, Category
# from .app.extensions import db

app = create_app()
#app.app_context().push()
with app.app_context():
    db.drop_all()
    db.create_all()

    # Creating the category for Starters
    starters = Category(name='Starters')
    pizza = Category(name='Pizza')
    subs = Category(name='Subs')
    meals = Category(name='Meals')

    db.session.add_all([starters, pizza, subs, meals])
    db.session.commit() 
    
    # Defining the parent categories and their subcategories
    parent_categories = {
        'Starters': ['Appetizers', 'French Fries', 'Wings', 'Salads'],
        'Pizza': ['Regular Pizza', 'Gourmet Pizza'],
        'Subs':['Hot Subs', 'Cold Subs', 'Wraps', 'Burgers'],
        'Meals':['Pastas', 'Veal', 'Chicken', 'Seafood', 'Baked Dishes', 'Sides', 'Kids']
    }

    # Create and add categories and subcategories to the database
    for parent_name, subcategory_names in parent_categories.items():
        # Creating the parent category 
        parent_category = Category(name=parent_name)
        db.session.add(parent_category)
        db.session.flush() # This will allow us to get the id of the parent category


        # Creating subcategories and add them to the session
        for subcategory_name in subcategory_names:
            subcategory = Category(name=subcategory_name, parent_id=parent_category.id)
            db.session.add(subcategory)
    # Committ all subcategories at once
    db.session.commit()


    # Defining menu items linked to their subcategories
    category_ids = {cat.name: cat.id for cat in Category.query.all()}

    # Creating menu items using the dictionary to get the correct category_ids
    menu_items = [
        # Appetizers list inside of Starters
        MenuItem(name='Bruschetta', price=9.50, category_id=category_ids['Appetizers']),
        MenuItem(name='Fried Calamari', price=11.00, category_id=category_ids['Appetizers']),
        MenuItem(name='Sweet Chili Fried Calamari', price=12.00, category_id=category_ids['Appetizers']),
        MenuItem(name='Mussels Marinara', price=10.00, category_id=category_ids['Appetizers']),
        MenuItem(name='Mozzarella Sticks (6)', price=8.50, category_id=category_ids['Appetizers']),
        MenuItem(name='Fried Ravioli (6)', price=8.50, category_id=category_ids['Appetizers']),
        MenuItem(name='Potato Skins', price=7.75, category_id=category_ids['Appetizers']),
        MenuItem(name='Garlic Knots (6)', price=5.00, category_id=category_ids['Appetizers']),
        MenuItem(name='Loaded Garlic Knots (6)', price=9.00, category_id=category_ids['Appetizers']),
        MenuItem(name='Loaded Nachos', price=12.00, category_id=category_ids['Appetizers']),
        MenuItem(name='Chicken Tenders & Fries', price=9.00, category_id=category_ids['Appetizers']), 
        MenuItem(name='Perogies', price=6.75, category_id=category_ids['Appetizers']),
        # French Fries list inside of Starters
        MenuItem(name='Regular', price=3.00, category_id=category_ids['French Fries']),
        MenuItem(name='Bacon Cheddar Cheese', price=6.00, category_id=category_ids['French Fries']),
        MenuItem(name='Loaded Texas Style', price=6.00, category_id=category_ids['French Fries']),
        MenuItem(name='Buffalo Cheese', price=6.00, category_id=category_ids['French Fries']),
        MenuItem(name='Disco Style', price=6.00, category_id=category_ids['French Fries']),
        MenuItem(name='Pizza Style', price=6.00, category_id=category_ids['French Fries']),
        # Wings list inside of Starters
        MenuItem(name='Jumbo Party Wings (6)', price=7.50, category_id=category_ids['Wings']),
        MenuItem(name='Jumbo Party Wings (12)', price=14.00, category_id=category_ids['Wings']),
        MenuItem(name='Boneless Wings (6)', price=7.50, category_id=category_ids['Wings']),
        # Salads list inside of Starters
        MenuItem(name='Tossed Salad', price=7.00, category_id=category_ids['Salads']),
        MenuItem(name='Caesar Salad', price=8.00, category_id=category_ids['Salads']),
        MenuItem(name='Greek Salad', price=10.00, category_id=category_ids['Salads']),
        MenuItem(name='Antipast Salad', price=10.00, category_id=category_ids['Salads']),
        MenuItem(name='Chef Salad', price=10.00, category_id=category_ids['Salads']),
        MenuItem(name='Buffalo Chicken', price=10.00, category_id=category_ids['Salads']),
        MenuItem(name='Breaded Chicken', price=10.00, category_id=category_ids['Salads']),
        MenuItem(name='Cheese Steak', price=10.00, category_id=category_ids['Salads']),
        MenuItem(name='Chicken Cheesesteak', price=10.00, category_id=category_ids['Salads']),

        # Cheese pizza and sicilian pizza inside of Pizza
        MenuItem(name='Cheese Pizza', price=13.25, category_id=category_ids['Regular Pizza']),
        MenuItem(name='Sicilian Pizza', price=22.00, category_id=category_ids['Regular Pizza']),
        # Subcategories for Gourmet Pizza
        MenuItem(name='German Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='White Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Taco Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Hawaiian Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Margarita Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Meat Lover Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Chicken Bacon Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='BBQ Chicken & Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Buffalo Chicken Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Sweet Chili Chicken Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='BLT Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Veggie Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Chicago Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Philly Cheese Steak Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='House Special Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Sloppy Joe Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Lasagna Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Thin Style Grandma Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        MenuItem(name='Angry Pizza', price=18.00, category_id=category_ids['Gourmet Pizza']),
        
        # Hot Subs list inside of Subs
        MenuItem(name='Cheesesteak', price=10.00, category_id=category_ids['Hot Subs']),
        MenuItem(name='California Cheesesteak', price= 10.50, category_id=category_ids['Hot Subs']),
        MenuItem(name='Chicken Cheesesteak', price=10.00, category_id=category_ids['Hot Subs']),
        MenuItem(name='California Chicken Cheesesteak', price=10.50, category_id=category_ids['Hot Subs']),
        MenuItem(name='Buffalo Chicken Cheesesteak', price=10.50, category_id=category_ids['Hot Subs']),
        MenuItem(name='Grilled Chicken', price=10.50, category_id=category_ids['Hot Subs']),
        MenuItem(name='Edgemont Grilled Chicken', price=11.75, category_id=category_ids['Hot Subs']),
        MenuItem(name='Chicken Bacon Ranch', price=10.50, category_id=category_ids['Hot Subs']),
        MenuItem(name='California Buffalo Chicken', price=10.50, category_id=category_ids['Hot Subs']),
        MenuItem(name='Fried Chicken', price=10.50, category_id=category_ids['Hot Subs']),
        MenuItem(name='Chicken Parmesan', price=11.00, category_id=category_ids['Hot Subs']),
        MenuItem(name='Meatball Parmesan', price=11.00, category_id=category_ids['Hot Subs']),
        MenuItem(name='Veal Parmesan', price=14.00, category_id=category_ids['Hot Subs']),
        MenuItem(name='Eggplant Parmesan', price=11.00, category_id=category_ids['Hot Subs']),
        MenuItem(name='Sausage Parmesan', price=11.00, category_id=category_ids['Hot Subs']),
        MenuItem(name='Gyro', price=10.00, category_id=category_ids['Hot Subs']),
        # Cold Subs list inside of Subs
        MenuItem(name='Italian', price=11.00, category_id=category_ids['Cold Subs']),
        MenuItem(name='Ham & Cheese', price=10.00, category_id=category_ids['Cold Subs']),
        MenuItem(name='Salami & Cheese', price=10.00, category_id=category_ids['Cold Subs']),
        MenuItem(name='Turkey & Cheese', price=10.00, category_id=category_ids['Cold Subs']),
        # Wraps list inside of Subs
        MenuItem(name='Buffalo Chicken Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='California Buffalo Chicken Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='Cheesesteak Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='California Cheesesteak Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='Chicken Cheesesteak Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='California Chicken Cheesesteak Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='Grilled Chicken', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='Italian Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='American Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='Turkey, Bacon & Cheese Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='House Wrap', price=10.25, category_id=category_ids['Wraps']),
        MenuItem(name='BLT Wrap', price=10.25, category_id=category_ids['Wraps']),
        # Burgers list inside of Subs
        MenuItem(name='Cheeseburger Deluxe', price=11.00, category_id=category_ids['Burgers']),
        MenuItem(name='Bacon Cheeseburger', price=13.00, category_id=category_ids['Burgers']),
        MenuItem(name='Pesto Cheeseburger', price=13.00, category_id=category_ids['Burgers']),
        MenuItem(name='Edgemont Cheeseburger', price=13.00, category_id=category_ids['Burgers']),
        MenuItem(name='Cowboy Cheeseburger', price=13.00, category_id=category_ids['Burgers']),
        MenuItem(name='Angry Cheeseburger', price=13.00, category_id=category_ids['Burgers']),

        
    ]

    db.session.add_all(menu_items)
    db.session.commit() # Final commit to save everything
    print(f"Number of categories: {Category.query.count()}") # Debugging print to check the number of categories
    print(f"Number of menu items: {MenuItem.query.count()}") # Debugging print to check the number of menu items
