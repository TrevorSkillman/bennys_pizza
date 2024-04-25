from flask import Blueprint, render_template, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/starters') # Dynamic route
def starters():
    # We need to get and display the items inside of starters
    starters = get_starters()
    return render_template('starters.html', starters=starters)

