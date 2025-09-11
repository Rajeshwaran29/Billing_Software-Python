from flask import Blueprint, render_template, redirect, request, url_for, flash
from db import get_db_connection

add_bp = Blueprint('add_user_api', __name__)


@add_bp.route('/staff_form')
def staff_form():

    return render_template("owner/add_staff.html")


@add_bp.route('/add_staff', methods=['POST'])
def add_staff():
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


    return redirect(url_for("add_user_api.staff_form"))
