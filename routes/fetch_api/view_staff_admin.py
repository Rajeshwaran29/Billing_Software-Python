from flask import Blueprint, render_template
import pymysql.cursors
from db import get_db_connection

view_staff_admin_bp = Blueprint("staff_admin_api", __name__)



@view_staff_admin_bp.route("/view_staff_by_admin")
def view_staff_by_admin():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM user WHERE role_type = 'staff'")
    rows = cursor.fetchall()

    print("Rows fetched from DB:", rows)   # DEBUG

    cursor.close()
    conn.close()

    return render_template("admin/view_staff_by_admin.html", users=rows)