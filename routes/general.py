from flask import Flask , render_template , request , url_for , Blueprint ,session , redirect ,flash
from db import get_db_connection


general_bp = Blueprint("general_api" , __name__ , url_prefix="/")

@general_bp.route('/')
def index():
    return render_template("index.html")

@general_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))

@general_bp.route("/signin" ,  methods = ['POST'])
def signin():
    employee_name = request.form.get("employee_name")
    employee_password = request.form.get("employee_password")
    selected_role = request.form.get("role")   # role from radio buttons

    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500

    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM user WHERE employee_name=%s AND employee_password=%s AND role_type=%s",
        (employee_name, employee_password, selected_role)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:

        session["user_employee_name"] = user["employee_name"]
        session["role_type"] = user["role_type"]

       
        if selected_role == "owner":
            return redirect(url_for("general_api.owner_dashboard"))
        elif selected_role == "admin":
            return redirect(url_for("general_api.admin_dashboard"))
        else:
            return redirect(url_for("general_api.staff_dashboard"))
    else:
        flash("Invalid credentials or role. Please try again.")
        return redirect(url_for("general_api.index"))

#owner dashboard#
@general_bp.route("/owner")
def owner_dashboard():
    return render_template("owner/home_own.html")

@general_bp.route("/owner/access")
def access_own():
    return render_template("owner/access_own.html")

@general_bp.route("/owner/access/add_staff")
def add_staff_by_owner():
    return render_template("owner/add_staff.html")

@general_bp.route("/owner/access/add_admin")
def add_admin_by_owner():
    return render_template("owner/add_admin.html")

@general_bp.route("/owner/access/view_staff")
def view_staff_by_owner():
    return render_template("owner/view_staff.html")




@general_bp.route("/owner/settings")
def settings_own():
    return render_template("owner/settings.html")

#owner dashboard complete

#admin dashboard#

@general_bp.route("/admin")
def admin_dashboard():
    return render_template("admin/access_admin.html")

@general_bp.route("/admin/access/add_staff_by_admin")
def add_staff_admin():
    return render_template("admin/add_staff_by_admin.html")

@general_bp.route("/admin/products/add_product")
def add_product_admin():
    return render_template("admin/add_product.html")

@general_bp.route("/admin/products")
def product_admin():
    return render_template("admin/Products_admin.html")


@general_bp.route("/admin/settings")
def settings_admin():
    return render_template("/admin/admin_settings.html")


#admin dashboard complete#


#staff_dashboard

@general_bp.route("/staff")
def staff_dashboard():
    return render_template("staff/staff_billing.html")

