from flask import Blueprint, render_template
import pymysql.cursors
from db import get_db_connection

view_product_staff_bp = Blueprint("view_product_staff_api", __name__)



@view_product_staff_bp.route("/view_product_staff")
def view_product_staff():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()

    print("Rows fetched from DB:", rows)   # DEBUG

    cursor.close()
    conn.close()

    return render_template("staff/staff_product_list.html", products=rows)