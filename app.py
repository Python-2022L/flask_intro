from flask import Flask, request
from tinydb import TinyDB, Query
app = Flask(__name__)

@app.route("/api/product")
def main():
    db = TinyDB('db.json')
    product = db.table('grocery')
    table = """<table border="1|1">
    <tr>
        <th>name</th>
        <th>Quantity</th>
        <th>Price</th>
        <th>Type</th>
    </tr>"""

    for item in product:
        table += f"""
        <tr>
            <td>{item['name']}</td>
            <td>{item['quantity']}</td>
            <td>{item['price']}</td>
            <td>{item['type']}</td>
        </tr>"""

    table += "</table>"
    return table

if __name__ == '__main__':
    app.run(debug=True, port='8080')