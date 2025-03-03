# from flask import Blueprint, render_template
# from app.models import Men, Women, Kids, Accessories, Shoes  # Correct import

# # Define Blueprint for views
# views_bp = Blueprint('views', __name__)

# # Index route to display products
# @views_bp.route('/')
# def index():
#     # Query all products from different categories
#     products_men = Men.query.all()
#     products_women = Women.query.all()
#     products_kids = Kids.query.all()
#     products_accessories = Accessories.query.all()
#     products_shoes = Shoes.query.all()  # Correct Shoes model reference

#     # Combine all products into one list
#     all_products = products_men + products_women + products_kids + products_accessories + products_shoes

#     # Render the homepage template and pass the products to the template
#     return render_template('index.html', products=all_products)

# @views_bp.route('/men')
# def men():
#     products_men = Men.query.all()
    
#     return render_template('men.html', products=products_men)

# @views_bp.route('/women')
# def women():
#     products_women = Women.query.all()
#     return render_template('women.html', products=products_women, category="Women")

# @views_bp.route('/kids')
# def kids():
#     products_kids = Kids.query.all()
#     return render_template('kids.html', products=products_kids, category="Kids")

# @views_bp.route('/accessories')
# def accessories():
#     products_accessories = Accessories.query.all()
#     return render_template('accessories.html', products=products_accessories, category="Accessories")

# @views_bp.route('/shoes')
# def shoes():
#     products_shoes = Shoes.query.all()  # Correct query
#     return render_template('shoes.html', products=products_shoes, category="Shoes")




from flask import Blueprint, render_template, abort
from app.models import Men, Women, Kids, Accessories, Shoes
from .models import Product
# Define Blueprint for views
views_bp = Blueprint('views', __name__)

# Map category names to their respective models
CATEGORY_MODELS = {
    'men': Men,
    'women': Women,
    'kids': Kids,
    'accessories': Accessories,
    'shoes': Shoes
}

# Index route to display all products
@views_bp.route('/')
def index():
    # Query all products from different categories
    all_products = []
    for model in CATEGORY_MODELS.values():
        all_products.extend(model.query.all())

    # Render the homepage template and pass all products to the template
    return render_template('index.html', products=all_products)

# Dynamic route to display products for a specific category
@views_bp.route('/category/<category_name>')
def category(category_name):
    # Get the model for the requested category
    model = CATEGORY_MODELS.get(category_name)
    if not model:
        abort(404)  # Return a 404 error if the category is invalid

    # Query products for the requested category
    products = model.query.all()
    return render_template('category.html', products=products, category_name=category_name.capitalize())

# Existing routes for backward compatibility
@views_bp.route('/men')
def men():
    return category('men')  # Reuse the dynamic route logic

@views_bp.route('/women')
def women():
    return category('women')  # Reuse the dynamic route logic

@views_bp.route('/kids')
def kids():
    return category('kids')  # Reuse the dynamic route logic

@views_bp.route('/Accessories')
def accessories():
    return category('accessories')  # Reuse the dynamic route logic

@views_bp.route('/Shoes')
def shoes():
    return category('shoes')  # Reuse the dynamic route logic
@views_bp.route('/product/<int:product_id>')
def product_details(product_id):
    # Query the product by ID
    product = Product.query.get_or_404(product_id)
    return render_template('product_details.html', product=product)