from flask import Blueprint, render_template, redirect, request, url_for, flash
from db import get_db_connection

add_user_bp = Blueprint('add_user_admin_api', __name__)


@add_user_bp.route('/staff_add_form')
def staff_add_form():

    return render_template("admin/add_staff_by_admin.html")


@add_user_bp.route('/add_staff_by_admin', methods=['POST'])
def add_staff_by_admin():
    employee_name = request.form.get("employee_name")
    mail = request.form.get("mail")
    mobile = request.form.get("mobile")
    address = request.form.get("address")
    role_type = request.form.get("role_type")
    employee_password = request.form.get("employee_password")

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO user (employee_name, mail, mobile, address, role_type, employee_password)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (employee_name, mail, mobile, address, role_type, employee_password)

    cursor.execute(sql, values)
    conn.commit()



    cursor.close()
    conn.close()

    flash(f"✅ Staff '{employee_name}' added successfully!", "success")


    return redirect(url_for("add_user_admin_api.staff_add_form"))
