from flask import Blueprint, render_template
import pymysql.cursors
from db import get_db_connection

view_product_admin_bp = Blueprint("view_product_admin_api", __name__)



@view_product_admin_bp.route("/view_product")
def view_product():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()

    print("Rows fetched from DB:", rows)   # DEBUG

    cursor.close()
    conn.close()

    return render_template("admin/view_product.html", products=rows)