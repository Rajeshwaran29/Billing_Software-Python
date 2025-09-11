from flask import Blueprint, render_template, redirect, request, url_for, flash
from db import get_db_connection

product_bp = Blueprint('add_product_api', __name__)


@product_bp.route('/add_product')
def product_add_form():

    return render_template("admin/add_product.html")


@product_bp.route('/add_product', methods=['POST'])
def add_product_admin():
    product_name = request.form.get("product_name")
    price = request.form.get("price")


    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
            INSERT INTO product(product_name , price) VALUES(%s ,%s)"""
    values = (product_name , price)

    cursor.execute(sql, values)
    conn.commit()



    cursor.close()
    conn.close()




    return redirect(url_for("add_product_api.product_add_form"))
