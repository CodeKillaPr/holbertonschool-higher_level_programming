from flask import Flask, render_template
import csv
import sqlite3

app = Flask(__name__)


def read_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            return list(csv.DictReader(csv_file))
    except FileNotFoundError:
        return None


def read_sql():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    except sqlite3.DatabaseError:
        return None


@app.route('/display/<source>/<int:product_id>')
def display_product(source, product_id=None):
    products = None
    if source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    if products is None:
        return render_template('product_display.html', error="Failed to read source")

    if product_id is not None:
        # Ensure product_id is compared correctly, assuming product['id'] is an integer
        products = [
            product for product in products if product['id'] == str(product_id)]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
