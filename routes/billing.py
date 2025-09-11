from flask import Blueprint, render_template, request, jsonify
from db import get_db_connection
import pymysql.cursors
from datetime import datetime

billing_bp = Blueprint("billing_api", __name__)

@billing_bp.route("/billing")
def billing_page():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT id, product_name, price FROM product")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("staff/staff_billing.html", rows=products)


@billing_bp.route("/search_product")
def search_product():
    name = request.args.get("name", "")
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT id, product_name, price FROM product WHERE product_name LIKE %s LIMIT 1", (f"%{name}%",))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({"product": product})


@billing_bp.route("/save_bill", methods=["POST"])
def save_bill():
    bill_datetime = datetime.now()
    product_name = request.form.get('product_name')
    price = request.form.get("price")
    quantity = request.form.get("quantity")
    total = request.form.get("total")

    conn = get_db_connection()
    cursor = conn.cursor()


    sql = """
        INSERT INTO bills (bill_datetime, product_name, price, quantity, total)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (bill_datetime, product_name, price, quantity, total)

    try:
        cursor.execute(sql, values)
        conn.commit()
        return "Bill Saved Successfully!"
    except Exception as e:
        conn.rollback()
        return f"Error: {e}"
    finally:
        cursor.close()
        conn.close()