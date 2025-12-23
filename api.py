from flask import Flask, jsonify, request
from src import database as db

app = Flask(__name__)

@app.route("/employees", methods=["GET"])
def get_employees():
    employees_from_db = db.get_all_employees()
    employees_list = [dict(emp) for emp in employees_from_db]
    return jsonify(employees_list), 200

@app.route("/clients", methods=["GET"])
def get_clients():
    clients_from_db = db.get_all_clients()
    clients_list = [dict(emp) for emp in clients_from_db]
    return jsonify(clients_list), 200

@app.route("/providers", methods=["GET"])
def get_providers():
    providers_from_db = db.get_all_providers()
    providers_list = [dict(emp) for emp in providers_from_db]
    return jsonify(providers_list), 200

@app.route("/products", methods=["GET"])
def get_products():
    products_from_db = db.get_all_products()
    products_list = [dict(emp) for emp in products_from_db]
    return jsonify(products_list), 200

@app.route("/sales", methods=["GET"])
def get_sales():
    sales_from_db = db.get_all_sales()
    sales_list = [dict(emp) for emp in sales_from_db]
    return jsonify(sales_list), 200

@app.route("/purchases", methods=["GET"])
def get_purchases():
    purchases_from_db = db.get_all_purchases()
    purchases_list = [dict(emp) for emp in purchases_from_db]
    return jsonify(purchases_list), 200

@app.route("/employee", methods=["POST"])
def add_employee():
    data = request.get_json()
    name = data.get("name")
    position = data.get("position")
    db.create_employee(name, position)
    return jsonify({"message": "Employee added successfully"}), 201

@app.route("/client", methods=["POST"])
def add_client():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    db.create_client(name, email, phone)
    return jsonify({"message": "Client added successfully"}), 201

@app.route("/provider", methods=["POST"])
def add_provider():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    field = data.get("field")
    db.create_client(name, email, phone, field)
    return jsonify({"message": "Provider added successfully"}), 201

@app.route("/product", methods=["POST"])
def add_product():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")
    provider = data.get("provider")
    db.create_product(name, description, price, stock, provider)
    return jsonify({"message": "Product added succesfully"}), 201

@app.route("/sale", methods=["POST"])
def add_sale():
    data = request.get_json()
    product_id = data.get("product_id")
    employee_id = data.get("employee_id")
    client_id = data.get("client_id")
    date = data.get("date")
    total = data.get("total")
    db.create_sale(client_id, product_id, employee_id, date, total)
    return jsonify({"message": "Sale added succesfully"}), 201

@app.route("/purchase", methods=["POST"])
def add_purchase():
    data = request.get_json()
    product_id = data.get("product_id")
    provider_id = data.get("provider_id")
    employee_id = data.get("employee_id")
    quantity = data.get("quantity")
    total_cost = data.get("total_cost")
    db.create_purchase(product_id, provider_id, employee, quantity, total_cost)
    return jsonify({"message": "Purchase added succesfully"}), 201


if __name__ == '__main__':
    app.run(debug=True)