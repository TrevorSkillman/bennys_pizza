from app import create_app, db
from app.models import MenuItem, Category
import json
# from .app.extensions import db

app = create_app()
#app.app_context().push()
with app.app_context():
    db.drop_all()
    db.create_all()

    # Creating the category 
    categories = [
        Category(name='Starters'),
        Category(name='Pizza'),
        Category(name='Strombolis'),
        Category(name='Subs'),
        Category(name='Meals'),
        Category(name='Desserts'),
        Category(name='Catering'),
    ]
    db.session.add_all(categories)
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
        parent_category = Category.query.filter_by(name=parent_name).first()
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
        MenuItem(name='Regular', price=3.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 3.00, 'Large': 5.00})),
        MenuItem(name='Bacon Cheddar Cheese', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00})),
        MenuItem(name='Loaded Texas Style', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00})),
        MenuItem(name='Buffalo Cheese', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00})),
        MenuItem(name='Disco Style', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00})),
        MenuItem(name='Pizza Style', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00})),
        # Wings list inside of Starters
        MenuItem(name='Jumbo Party Wings (6)', price=7.50, category_id=category_ids['Wings']),
        MenuItem(name='Jumbo Party Wings (12)', price=14.00, category_id=category_ids['Wings']),
        MenuItem(name='Boneless Wings (6)', price=7.50, category_id=category_ids['Wings'], sizes=json.dumps({'(6)': 7.50, '(12)': 15.00})),
        # Salads list inside of Starters
        MenuItem(name='Tossed Salad', price=7.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 7.00, 'Large': 8.00})),
        MenuItem(name='Caesar Salad', price=8.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 8.00, 'Large': 9.00})),
        MenuItem(name='Greek Salad', price=10.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 10.00, 'Large': 12.00})),
        MenuItem(name='Antipast Salad', price=10.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 10.00, 'Large': 12.00})),
        MenuItem(name='Chef Salad', price=10.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 10.00, 'Large': 12.00})),
        MenuItem(name='Buffalo Chicken', price=10.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 10.00, 'Large': 12.00})),
        MenuItem(name='Breaded Chicken', price=10.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 10.00, 'Large': 12.00})),
        MenuItem(name='Cheese Steak', price=10.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 10.00, 'Large': 12.00})),
        MenuItem(name='Chicken Cheesesteak', price=10.00, category_id=category_ids['Salads'], sizes=json.dumps({'Small': 10.00, 'Large': 12.00})),

        # Cheese pizza and sicilian pizza inside of Pizza
        MenuItem(name='Cheese Pizza', price=13.25, category_id=category_ids['Regular Pizza'], sizes=json.dumps({'Personal': 13.25, 'Medium': 14.25, 'Large': 15.25})),
        MenuItem(name='Sicilian Pizza', price=22.00, category_id=category_ids['Regular Pizza']),
        # Subcategories for Gourmet Pizza
        MenuItem(name='German Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='White Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Taco Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Hawaiian Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Margarita Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Meat Lover Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Chicken Bacon Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='BBQ Chicken & Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Buffalo Chicken Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Sweet Chili Chicken Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='BLT Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Veggie Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Chicago Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Philly Cheese Steak Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='House Special Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Sloppy Joe Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Lasagna Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Thin Style Grandma Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),
        MenuItem(name='Angry Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00})),

        # Strombolis list inside of Strombolis
        MenuItem(name='German', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='Special Cheese Steak', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='Veggie', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='Regular Stromboli', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='Buffalo Chicken', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='Chicken Bacon Ranch Stromboli', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='Special Chicken Cheesesteak Stromboli', price=12.00,  category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='BBQ Chicken Ranch Stromboli', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='Sausege Pepper & Onions', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),
        MenuItem(name='Calzone', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00})),

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

        # Pastas list inside of Meals
        MenuItem(name='Garlic & Olive Oil', price=12.00, category_id=category_ids['Pastas']),
        MenuItem(name='Broccoli, Garlic, Olive Oil', price=13.00, category_id=category_ids['Pastas']),
        MenuItem(name='Alfredo Sauice', price=15.75, category_id=category_ids['Pastas']),
        MenuItem(name='Carbonara Sauce', price=16.75, category_id=category_ids['Pastas']),
        MenuItem(name='Spaghetti & Meatballs', price=15.75, category_id=category_ids['Pastas']),
        MenuItem(name='Bolegnese', price=15.75, category_id=category_ids['Pastas']),
        MenuItem(name='Creamy Pesto Sauce', price=15.75, category_id=category_ids['Pastas']),
        MenuItem(name='Penne Alla Vodka', price=15.75, category_id=category_ids['Pastas']),
        MenuItem(name='Marinara', price=12.00, category_id=category_ids['Pastas']),

        # Veal list inside of Meals
        MenuItem(name="Veal Parmesan", price=20.00, category_id=category_ids['Veal']),
        
        # Chicken list inside of Meals
        MenuItem(name='Chicken Parmesan', price=18.00, category_id=category_ids['Chicken']),
        MenuItem(name='Chicken Scarpariello', price=18.00, category_id=category_ids['Chicken']),
        MenuItem(name='Chicken Marsala', price=18.00, category_id=category_ids['Chicken']),
        MenuItem(name='Chicken Karina', price=18.00, category_id=category_ids['Chicken']),
        MenuItem(name='Chicken Pasta', price=18.00, category_id=category_ids['Chicken']),
        MenuItem(name='Chicken Francese', price=19.00, category_id=category_ids['Chicken']),

        # Seafood list inside of Seafood
        MenuItem(name='Baby Clam Sauce', price=18.50, category_id=category_ids['Seafood']),
        MenuItem(name='Srimp Alfrdeo', price=20.00, category_id=category_ids['Seafood']),
        MenuItem(name='Shrimp Ala Vodka', price=20.00, category_id=category_ids['Seafood']),
        MenuItem(name='Shrimp Scampi', price=20.00, category_id=category_ids['Seafood']),
        MenuItem(name='Mussels Marinara', price=20.00, category_id=category_ids['Seafood']),
        MenuItem(name='Seafood Fra Diavolo', price=23.00, category_id=category_ids['Seafood']),

        # Baked Dishes inside of Baked Dishes
        MenuItem(name='Cheese Ravioli (6)', price=14.00, category_id=category_ids['Baked Dishes']),
        MenuItem(name='Stuffed Shells (6)', price=14.00, category_id=category_ids['Baked Dishes']),
        MenuItem(name='Manicotti (4)', price=14.00, category_id=category_ids['Baked Dishes']),
        MenuItem(name='Baked Zita', price=15.50, category_id=category_ids['Baked Dishes']),
        MenuItem(name='Lasagna', price=17.00, category_id=category_ids['Baked Dishes']),
        MenuItem(name='Eggplant Parmigiana', price=17.00, category_id=category_ids['Baked Dishes']),
        MenuItem(name='Eggplant Rollatini', price=17.50, category_id=category_ids['Baked Dishes']),

        # Sides inside of the Sides subcategory
        MenuItem(name='Meatballs', price=5.00, category_id=category_ids['Sides']), 
        MenuItem(name='Sausage', price=5.00, category_id=category_ids['Sides']),
        MenuItem(name='Cheesy Garlic Bread', price=5.00, category_id=category_ids['Sides']),
        MenuItem(name='Garlic Bread', price=3.50, category_id=category_ids['Sides']),

        # Kids menu inside of kids subcategory
        MenuItem(name='Chicken Tenders & Fries', price=6.75, category_id=category_ids['Kids']),
        MenuItem(name='Cheese Slice and French Fries', price=3.25, category_id=category_ids['Kids']),
        MenuItem(name='Spaghetti & Sauce', price=5.75, category_id=category_ids['Kids']),
        MenuItem(name='Spaghetti & Meatballs', price=6.75, category_id=category_ids['Kids']),
        MenuItem(name='Cheese Ravioli', price=6.75, category_id=category_ids['Kids']),

        # Desserts list inside of Desserts
        MenuItem(name='Cannoli', price=5.00, category_id=category_ids['Desserts']),
        MenuItem(name='Zeppolis', price='5.00', category_id=category_ids['Desserts']),
        MenuItem(name='Tiramisu', price=5.00, category_id=category_ids['Desserts']),
        MenuItem(name='Cannoli Zeppolis', price=5.00, category_id=category_ids['Desserts']),
        MenuItem(name='Tartufo', price=5.00, category_id=category_ids['Desserts']),

        # Catering list inside of Catering
        MenuItem(name='Chicken Parmigiana', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 90.00})),
        MenuItem(name='Baked Ziti', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00})),
        MenuItem(name='Eggplant Parmigiana', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 90.00})),
        MenuItem(name='Eggplant Rollatini', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 90.00})),
        MenuItem(name='Chicken Marsala', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 85.00})),
        MenuItem(name='Chicken Francese', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 75.00, 'Full Tray': 110.00})),
        MenuItem(name='Veal Parmigiana', price=75.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 75.00, 'Full Tray': 95.00})),
        MenuItem(name='Veal Marsala', price=75.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 75.00, 'Full Tray': 95.00})),
        MenuItem(name='Penne Ala Vodka', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00})),
        MenuItem(name='Spaghetti', price=80.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 80.00, 'Full Tray': 100.00})),
        MenuItem(name='Spaghetti Alfredo', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00})),
        MenuItem(name='Raviolis', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00})),
        MenuItem(name='Manicotti', price=50.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 50.00, 'Full Tray': 65.00})),
        MenuItem(name='Stuffed Shells', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00})),
        MenuItem(name='Meatballs', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00})),
        MenuItem(name='Sabrinas Lasagna', price=65.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 65.00, 'Full Tray': 100.00})),
        MenuItem(name='Tossed Salad', price=40.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 40.00, 'Full Tray': 50.00})),
        MenuItem(name='Antipasto Salad', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 75.00})),
        MenuItem(name='Chef Salad', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 75.00})),
        MenuItem(name='Garlic Knots', price=40.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 40.00, 'Full Tray': 55.00})),
    ]

    db.session.add_all(menu_items)
    db.session.commit() # Final commit to save everything
    print(f"Number of categories: {Category.query.all()}") # Debugging print to check the number of categories
    print(f"Number of menu items: {MenuItem.query.all()}") # Debugging print to check the number of menu items
