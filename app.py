from flask import Flask , render_template ,jsonify
from db import get_db_connection
from routes.add_api.add_user_owner import add_bp
from routes.add_api.add_admin_owner import admin_bp
from routes.add_api.add_product import product_bp
from routes.add_api.add_user_admin import add_user_bp
from routes.general import general_bp
from routes.fetch_api.view_user_owner import view_owner_user_bp
from routes.fetch_api.view_user_admin import view_owner_admin_bp
from routes.fetch_api.view_staff_admin import view_staff_admin_bp
from routes.fetch_api.view_product import view_product_admin_bp
from routes.billing import billing_bp


app = Flask(__name__)
app.secret_key = "your_super_secret_key"


app.register_blueprint(add_bp ,url_prefix="")
app.register_blueprint(admin_bp , url_prefix="")
app.register_blueprint(product_bp , url_prefix="")
app.register_blueprint(general_bp , url_prefix="")
app.register_blueprint(add_user_bp , url_prefix="")
app.register_blueprint(view_owner_user_bp , url_prefix="")
app.register_blueprint(view_owner_admin_bp , url_prefix = "")
app.register_blueprint(view_staff_admin_bp,url_prefix = "")
app.register_blueprint(view_product_admin_bp , url_prefix = "")
app.register_blueprint(billing_bp , url_prefix="")

@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)
