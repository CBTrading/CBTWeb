from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object("config")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html.j2"), 404

from app.products.views import products as products_module

app.register_blueprint(products_module)
