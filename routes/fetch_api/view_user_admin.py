from flask import Blueprint, render_template
import pymysql.cursors
from db import get_db_connection

view_owner_admin_bp = Blueprint("view_admin_api", __name__)



@view_owner_admin_bp.route("/view_admin")
def view_admin_owner():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM user WHERE role_type = 'admin'")
    rows = cursor.fetchall()

    print("Rows fetched from DB:", rows)   # DEBUG

    cursor.close()
    conn.close()

    return render_template("owner/view_admin.html", users=rows)