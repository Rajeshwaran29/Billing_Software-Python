from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import get_db_connection


admin_bp = Blueprint("admin_api", __name__)

@admin_bp.route("/admin_form")
def admin_form():
    return render_template("owner/add_admin.html")


@admin_bp.route("/add_admin", methods=["POST"])
def add_admin():
    employee_name = request.form.get("employee_name")
    mail = request.form.get("mail")
    mobile = request.form.get("mobile")
    address = request.form.get("address")
    role_type = "admin"   # force role_type to admin
    employee_password = request.form.get("employee_password")

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO user (employee_name, mail, mobile, address, role_type, employee_password)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (employee_name, mail, mobile, address, role_type, employee_password)

    try:
        cursor.execute(sql, values)
        conn.commit()
        flash(f"✅ Admin '{employee_name}' added successfully!", "success")
    except Exception as e:
        conn.rollback()
        flash(f"❌ Error adding admin: {str(e)}", "danger")
    finally:
        cursor.close()
        conn.close()


    return redirect(url_for("admin_api.admin_form"))
