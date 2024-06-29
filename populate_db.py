"""
This populates the database for Bennys Pizza. 
It creates categories, subcategories, and menu items with associated data.
"""

from app import create_app, db
from app.models import MenuItem, Category
import json

app = create_app()
with app.app_context():
    # Dropping all existing tables and creates new ones
    db.drop_all()
    db.create_all()

    # Creating the main categories
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


    # Mapping category names to their ids.
    category_ids = {cat.name: cat.id for cat in Category.query.all()}

    # Creating menu items using the dictionary to get the correct category_ids
    menu_items = [
        # Appetizers list inside of Starters
        MenuItem(name='Bruschetta', price=9.50, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Fried Calamari', price=11.00, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Sweet Chili Fried Calamari', price=12.00, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Mussels Marinara', price=10.00, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Mozzarella Sticks (6)', price=8.50, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Fried Ravioli (6)', price=8.50, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Potato Skins', price=7.75, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Garlic Knots (6)', price=5.00, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Loaded Garlic Knots (6)', price=9.00, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Loaded Nachos', price=12.00, category_id=category_ids['Appetizers'], description=None),
        MenuItem(name='Chicken Tenders & Fries', price=9.00, category_id=category_ids['Appetizers'], description=None), 
        MenuItem(name='Perogies', price=6.75, category_id=category_ids['Appetizers'], description=None),
        # French Fries list inside of Starters
        MenuItem(name='Regular', price=3.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 3.00, 'Large': 5.00}), description=None),
        MenuItem(name='Bacon Cheddar Cheese', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00}), description=None),
        MenuItem(name='Loaded Texas Style', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00}), description=None),
        MenuItem(name='Buffalo Cheese', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00}), description=None),
        MenuItem(name='Disco Style', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00}), description=None),
        MenuItem(name='Pizza Style', price=6.00, category_id=category_ids['French Fries'], sizes=json.dumps({'Small': 6.00, 'Large': 8.00}), description=None),
        # Wings list inside of Starters
        MenuItem(name='Jumbo Party Wings (6)', price=None, category_id=category_ids['Wings'], description='Hot, Mild, BBQ, Hot Honey, Honey BBQ, Honey Musterd, Sweet Chili, Garlic Parmesan, Old Bay Hot'),
        MenuItem(name='Jumbo Party Wings (12)', price=None, category_id=category_ids['Wings'], description='Hot, Mild, BBQ, Hot Honey, Honey BBQ, Honey Musterd, Sweet Chili, Garlic Parmesan, Old Bay Hot'),
        MenuItem(name='Boneless Wings (6)', price=7.50, category_id=category_ids['Wings'], sizes=json.dumps({'(6)': 7.50, '(12)': 15.00}), description='Hot, Mild, BBQ, Hot Honey, Honey BBQ, Honey Musterd, Sweet Chili, Garlic Parmesan, Old Bay Hot'),
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
        MenuItem(name='German Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Steak, Pepperoni, Onions, Peppers'),
        MenuItem(name='White Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Ricotta, Mozzarella +1 Topping'),
        MenuItem(name='Taco Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Beef, Lettuce, Tomatoes, Onions, Mild Sauce'),
        MenuItem(name='Hawaiian Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Pinapples, Ham'),
        MenuItem(name='Margarita Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Juicy Plum Tomatoes, Garlic, Basil & Fresh Mozzarella'),
        MenuItem(name='Meat Lover Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description=None),
        MenuItem(name='Chicken Bacon Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description=None),
        MenuItem(name='BBQ Chicken & Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description=None),
        MenuItem(name='Buffalo Chicken Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Chicken, Hot Sauce & Ranch'),
        MenuItem(name='Sweet Chili Chicken Ranch Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description=None),
        MenuItem(name='BLT Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Lettuce, Tomato, Bacon, Mayo'),
        MenuItem(name='Veggie Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Onions, Peppers, Mushrooms, Tomatoes, Broccoli'),
        MenuItem(name='Chicago Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Pepperoni, Sausage, Ham, Ground Beef & Extra Cheese'),
        MenuItem(name='Philly Cheese Steak Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Chopped Steak with Fried Onions'),
        MenuItem(name='House Special Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Mushrooms, Pepperoni, Olives & Sausage'),
        MenuItem(name='Sloppy Joe Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Manwich Sauce, Ground Beef, Mozzarella'),
        MenuItem(name='Lasagna Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Ground Beef, Ricotta & Marinara Sauce'),
        MenuItem(name='Thin Style Grandma Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Cheese Sauce, Fresh Basil, Garlic'),
        MenuItem(name='Angry Pizza', price=18.00, category_id=category_ids['Gourmet Pizza'], sizes=json.dumps({'Personal': 18.00, 'Medium': 20.00, 'Large': 22.00}), description='Jalapeno & Cherry Peppers'),

        # Strombolis list inside of Strombolis
        MenuItem(name='German', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description='Steak, Pepperoni, Onions & Green Peppers'),
        MenuItem(name='Special Cheese Steak', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description='Steak, Mushrooms, Onions & Green Peppers'),
        MenuItem(name='Veggie', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description='Mushrooms, Green Peppers & Onions, Tomatoes, Broccoli'),
        MenuItem(name='Regular Stromboli', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description='Ham, Salami, Pepperoni, Cheese, Sausage, Peppers & Onions'),
        MenuItem(name='Buffalo Chicken', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description='Chicken, Hot Sauce & Ranch'),
        MenuItem(name='Chicken Bacon Ranch Stromboli', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description=None),
        MenuItem(name='Special Chicken Cheesesteak Stromboli', price=12.00,  category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description='Mushrooms, Onions & Peppers'),
        MenuItem(name='BBQ Chicken Ranch Stromboli', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description=None),
        MenuItem(name='Sausege Pepper & Onions', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description=None),
        MenuItem(name='Calzone', price=12.00, category_id=category_ids['Strombolis'], sizes=json.dumps({'Mini': 12.00, 'Med': 18.00, 'Lg': 20.00}), description='Ricotta, Mozzarella'),

        # Hot Subs list inside of Subs
        MenuItem(name='Cheesesteak', price=10.00, category_id=category_ids['Hot Subs'], description='Each Additional Topping $0.50'),
        MenuItem(name='California Cheesesteak', price= 10.50, category_id=category_ids['Hot Subs'], description='Lettuce, Tomato, Onions & Mayo'),
        MenuItem(name='Chicken Cheesesteak', price=10.00, category_id=category_ids['Hot Subs'], description='Each Additional Topping $0.50'),
        MenuItem(name='California Chicken Cheesesteak', price=10.50, category_id=category_ids['Hot Subs'], description='Lettuce, Tomato, Onions & Mayo'),
        MenuItem(name='Buffalo Chicken Cheesesteak', price=10.50, category_id=category_ids['Hot Subs'], description='Chicken, Hot Sauce & Ranch'),
        MenuItem(name='Grilled Chicken', price=10.50, category_id=category_ids['Hot Subs'], description='Lettuce, Tomato, Onions & Mayo'),
        MenuItem(name='Edgemont Grilled Chicken', price=11.75, category_id=category_ids['Hot Subs'], description='Mozzarella, Roasted Peppers & Balsamic Dressing'),
        MenuItem(name='Chicken Bacon Ranch', price=10.50, category_id=category_ids['Hot Subs'], description=None),
        MenuItem(name='California Buffalo Chicken', price=10.50, category_id=category_ids['Hot Subs'], description='Breaded Chicken, Hot Sauce, Ranch, Lettuce, Tomato & Onion'),
        MenuItem(name='Fried Chicken', price=10.50, category_id=category_ids['Hot Subs'], description='Lettuce, Tomato, Onions & Mayo'),
        MenuItem(name='Chicken Parmesan', price=11.00, category_id=category_ids['Hot Subs'], description=None),
        MenuItem(name='Meatball Parmesan', price=11.00, category_id=category_ids['Hot Subs'], description=None),
        MenuItem(name='Veal Parmesan', price=14.00, category_id=category_ids['Hot Subs'], description=None),
        MenuItem(name='Eggplant Parmesan', price=11.00, category_id=category_ids['Hot Subs'], description=None),
        MenuItem(name='Sausage Parmesan', price=11.00, category_id=category_ids['Hot Subs'], description='Mozzrella Cheese, Green Peppers & Onions'),
        MenuItem(name='Gyro', price=10.00, category_id=category_ids['Hot Subs'], description=None),
        # Cold Subs list inside of Subs
        MenuItem(name='Italian', price=11.00, category_id=category_ids['Cold Subs'], description=None),
        MenuItem(name='Ham & Cheese', price=10.00, category_id=category_ids['Cold Subs'], description=None),
        MenuItem(name='Salami & Cheese', price=10.00, category_id=category_ids['Cold Subs'], description=None),
        MenuItem(name='Turkey & Cheese', price=10.00, category_id=category_ids['Cold Subs'], description=None),
        # Wraps list inside of Subs
        MenuItem(name='Buffalo Chicken Wrap', price=10.25, category_id=category_ids['Wraps'], description='Breaded Chicken, Hot Sauce, Ranch'),
        MenuItem(name='California Buffalo Chicken Wrap', price=10.25, category_id=category_ids['Wraps'], description='Breaded Chicken, Hot Sauce, Ranch, Lettuce, Tomato & Onion'),
        MenuItem(name='Cheesesteak Wrap', price=10.25, category_id=category_ids['Wraps'], description='Steak with Cheese'),
        MenuItem(name='California Cheesesteak Wrap', price=10.25, category_id=category_ids['Wraps'], description='Lettuce, Tomato, Onion & Mayo'),
        MenuItem(name='Chicken Cheesesteak Wrap', price=10.25, category_id=category_ids['Wraps'], description='Chicken with Cheese'),
        MenuItem(name='California Chicken Cheesesteak Wrap', price=10.25, category_id=category_ids['Wraps'], description='Lettuce, Tomato, Onion & Mayo'),
        MenuItem(name='Grilled Chicken', price=10.25, category_id=category_ids['Wraps'], description='Lettuce, Tomato, Onion & Mayo'),
        MenuItem(name='Italian Wrap', price=10.25, category_id=category_ids['Wraps'], description='Ham, Salami, Capicola, Provolone, Lettuce, Tomato, Onions & Mayo'),
        MenuItem(name='American Wrap', price=10.25, category_id=category_ids['Wraps'], description='Ham, Salami & Cheese with Lettuce, Tomato, Onions & Mayo'),
        MenuItem(name='Turkey, Bacon & Cheese Wrap', price=10.25, category_id=category_ids['Wraps'], description='Lettuce, Tomato, Onions & Mayo'),
        MenuItem(name='House Wrap', price=10.25, category_id=category_ids['Wraps'], description='Ham, Salami, Capicola, Pepperoni & Provolone with Lettuce, Tomato, Onions & Mayo'),
        MenuItem(name='BLT Wrap', price=10.25, category_id=category_ids['Wraps'], description='Bacon, Lettuce, Tomato & Mayo'),
        # Burgers list inside of Subs
        MenuItem(name='Cheeseburger Deluxe', price=11.00, category_id=category_ids['Burgers'], description='Lettuce, Tomato, Onions & Mayo w/ Fries'),
        MenuItem(name='Bacon Cheeseburger', price=13.00, category_id=category_ids['Burgers'], description='Bacon, Lettuce, Tomato & Mayo w/ Fries'),
        MenuItem(name='Pesto Cheeseburger', price=13.00, category_id=category_ids['Burgers'], description='Tomato, Pesto & Fresh Mozzarella w/ Fries'),
        MenuItem(name='Edgemont Cheeseburger', price=13.00, category_id=category_ids['Burgers'], description='Roasted Peppers, Fresh Mozzarella, Tomatoes & House Dressing w/ Fries'),
        MenuItem(name='Cowboy Cheeseburger', price=13.00, category_id=category_ids['Burgers'], description='Bacon, BBQ Sauce, Lettuce, Tomato & Fried Onions w/ Fries'),
        MenuItem(name='Angry Cheeseburger', price=13.00, category_id=category_ids['Burgers'], description='Lettuce, Tomato, Onions, Mayo & Jalapeno Peppers w/ Fries'),

        # Pastas list inside of Meals
        MenuItem(name='Garlic & Olive Oil', price=12.00, category_id=category_ids['Pastas'], description='Choice of Penne, Spaghetti, Cavatelli or Tortellini'),
        MenuItem(name='Broccoli, Garlic, Olive Oil', price=13.00, category_id=category_ids['Pastas'], description='Choice of Penne, Spaghetti, Cavatelli or Tortellini'),
        MenuItem(name='Alfredo Sauice', price=15.75, category_id=category_ids['Pastas'], description='Choice of Penne, Spaghetti, Cavatelli or Tortellini'),
        MenuItem(name='Carbonara Sauce', price=16.75, category_id=category_ids['Pastas'], description='Choice of Penne, Spaghetti, Cavatelli or Tortellini'),
        MenuItem(name='Spaghetti & Meatballs', price=15.75, category_id=category_ids['Pastas'], description=None),
        MenuItem(name='Bolegnese', price=15.75, category_id=category_ids['Pastas'], description='Choice of Penne, Spaghetti, Cavatelli or Tortellini'),
        MenuItem(name='Creamy Pesto Sauce', price=15.75, category_id=category_ids['Pastas'], description='Choice of Penne, Spaghetti, Cavatelli or Tortellini'),
        MenuItem(name='Penne Alla Vodka', price=15.75, category_id=category_ids['Pastas'], description='Choice of Penne, Spaghetti, Cavatelli or Tortellini'),
        MenuItem(name='Marinara', price=12.00, category_id=category_ids['Pastas'], description='Choice of Penne, Spaghetti, Cavatelli or Tortellini'),

        # Veal list inside of Meals
        MenuItem(name="Veal Parmesan", price=20.00, category_id=category_ids['Veal'], description=None),
        
        # Chicken list inside of Meals
        MenuItem(name='Chicken Parmesan', price=18.00, category_id=category_ids['Chicken'], description=None),
        MenuItem(name='Chicken Scarpariello', price=18.00, category_id=category_ids['Chicken'], description='Chicken with Mushrooms & Peppers in a White Wine Sauce'),
        MenuItem(name='Chicken Marsala', price=18.00, category_id=category_ids['Chicken'], description='Chicken Sauteed with Mushrooms in a Marsala Wine Sauce'),
        MenuItem(name='Chicken Karina', price=18.00, category_id=category_ids['Chicken'], description='Chicken Sauteed with Red Onions, Roasted Red Peppers, Topped with Feta Cheese in White Wine Sauce'),
        MenuItem(name='Chicken Pasta', price=18.00, category_id=category_ids['Chicken'], description='In a Broccoli, Garlic & Olive Oil Sauce'),
        MenuItem(name='Chicken Francese', price=19.00, category_id=category_ids['Chicken'], description=None),

        # Seafood list inside of Seafood
        MenuItem(name='Baby Clam Sauce', price=18.50, category_id=category_ids['Seafood'], description='Red or White Sauce'),
        MenuItem(name='Srimp Alfrdeo', price=20.00, category_id=category_ids['Seafood'], description=None),
        MenuItem(name='Shrimp Ala Vodka', price=20.00, category_id=category_ids['Seafood'], description=None),
        MenuItem(name='Shrimp Scampi', price=20.00, category_id=category_ids['Seafood'], description=None),
        MenuItem(name='Mussels Marinara', price=20.00, category_id=category_ids['Seafood'], description=None),
        MenuItem(name='Seafood Fra Diavolo', price=23.00, category_id=category_ids['Seafood'], description='Shrimp & Scallops in a Spicy Marinara Sauce'),

        # Baked Dishes inside of Baked Dishes
        MenuItem(name='Cheese Ravioli (6)', price=14.00, category_id=category_ids['Baked Dishes'], description=None),
        MenuItem(name='Stuffed Shells (6)', price=14.00, category_id=category_ids['Baked Dishes'], description=None),
        MenuItem(name='Manicotti (4)', price=14.00, category_id=category_ids['Baked Dishes'], description=None),
        MenuItem(name='Baked Zita', price=15.50, category_id=category_ids['Baked Dishes'], description=None),
        MenuItem(name='Lasagna', price=17.00, category_id=category_ids['Baked Dishes'], description=None),
        MenuItem(name='Eggplant Parmigiana', price=17.00, category_id=category_ids['Baked Dishes'], description=None),
        MenuItem(name='Eggplant Rollatini', price=17.50, category_id=category_ids['Baked Dishes'], description=None),

        # Sides inside of the Sides subcategory
        MenuItem(name='Meatballs', price=5.00, category_id=category_ids['Sides'], description=None), 
        MenuItem(name='Sausage', price=5.00, category_id=category_ids['Sides'], description=None),
        MenuItem(name='Cheesy Garlic Bread', price=5.00, category_id=category_ids['Sides'], description=None),
        MenuItem(name='Garlic Bread', price=3.50, category_id=category_ids['Sides'], description=None),

        # Kids menu inside of kids subcategory
        MenuItem(name='Chicken Tenders & Fries', price=6.75, category_id=category_ids['Kids'], description=None),
        MenuItem(name='Cheese Slice and French Fries', price=3.25, category_id=category_ids['Kids'], description=None),
        MenuItem(name='Spaghetti & Sauce', price=5.75, category_id=category_ids['Kids'], description=None),
        MenuItem(name='Spaghetti & Meatballs', price=6.75, category_id=category_ids['Kids'], description=None),
        MenuItem(name='Cheese Ravioli', price=6.75, category_id=category_ids['Kids'], description=None),

        # Desserts list inside of Desserts
        MenuItem(name='Cannoli', price=5.00, category_id=category_ids['Desserts'], description=None),
        MenuItem(name='Zeppolis', price='5.00', category_id=category_ids['Desserts'], description=None),
        MenuItem(name='Tiramisu', price=5.00, category_id=category_ids['Desserts'], description=None),
        MenuItem(name='Cannoli Zeppolis', price=5.00, category_id=category_ids['Desserts'], description=None),
        MenuItem(name='Tartufo', price=5.00, category_id=category_ids['Desserts'], description=None),

        # Catering list inside of Catering
        MenuItem(name='Chicken Parmigiana', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 90.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Baked Ziti', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Eggplant Parmigiana', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 90.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Eggplant Rollatini', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 90.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Chicken Marsala', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 85.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Chicken Francese', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 75.00, 'Full Tray': 110.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Veal Parmigiana', price=75.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 75.00, 'Full Tray': 95.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Veal Marsala', price=75.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 75.00, 'Full Tray': 95.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Penne Ala Vodka', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Spaghetti', price=80.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 80.00, 'Full Tray': 100.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Spaghetti Alfredo', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Raviolis', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Manicotti', price=50.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 50.00, 'Full Tray': 65.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Stuffed Shells', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Meatballs', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 80.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Sabrinas Lasagna', price=65.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 65.00, 'Full Tray': 100.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Tossed Salad', price=40.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 40.00, 'Full Tray': 50.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Antipasto Salad', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 75.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Chef Salad', price=60.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 60.00, 'Full Tray': 75.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
        MenuItem(name='Garlic Knots', price=40.00, category_id=category_ids['Catering'], sizes=json.dumps({'Half Tray': 40.00, 'Full Tray': 55.00}), description='1/2 Tray Serves 6 People - Full Tray Serves 12 People'),
    ]

    db.session.add_all(menu_items)
    db.session.commit() # Final commit to save everything
    print(f"Number of categories: {Category.query.all()}") # Debugging print to check the number of categories
    print(f"Number of menu items: {MenuItem.query.all()}") # Debugging print to check the number of menu items
