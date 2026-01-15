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
    clients_list = [dict(cli) for cli in clients_from_db]
    return jsonify(clients_list), 200

@app.route("/providers", methods=["GET"])
def get_providers():
    providers_from_db = db.get_all_providers()
    providers_list = [dict(prv) for prv in providers_from_db]
    return jsonify(providers_list), 200

@app.route("/products", methods=["GET"])
def get_products():
    products_from_db = db.get_all_products()
    products_list = [dict(prd) for prd in products_from_db]
    return jsonify(products_list), 200

@app.route("/sales", methods=["GET"])
def get_sales():
    sales_from_db = db.get_all_sales()
    sales_list = [dict(sal) for sal in sales_from_db]
    return jsonify(sales_list), 200

@app.route("/purchases", methods=["GET"])
def get_purchases():
    purchases_from_db = db.get_all_purchases()
    purchases_list = [dict(pur) for pur in purchases_from_db]
    return jsonify(purchases_list), 200

@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = db.get_employee(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(dict(employee)), 200

@app.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    client = db.get_client(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify(dict(client)), 200

@app.route("/providers/<int:provider_id>", methods=["GET"])
def get_provider(provider_id):
    provider = db.get_provider(provider_id)
    if not provider:
        return jsonify({"error": "Provider not found"}), 404
    return jsonify(dict(provider)), 200

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = db.get_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(dict(product)), 200

@app.route("/sales/<int:sale_id>", methods=["GET"])
def get_sale(sale_id):
    sale = db.get_sale(sale_id)
    if not sale:
        return jsonify({"error": "Sale not found"}), 404
    return jsonify(dict(sale)), 200

@app.route("/purchases/<int:purchase_id>", methods=["GET"])
def get_purchase(purchase_id):
    purchase = db.get_purchase(purchase_id)
    if not purchase:
        return jsonify({"error": "Purchase not found"}), 404
    return jsonify(dict(purchase)), 200

@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("role"):
        return jsonify({"error": "Missing required fields"}), 400

    name = data.get("name")
    role = data.get("role")
    db.create_employee(name, role)
    return jsonify({"message": "Employee added successfully"}), 201

@app.route("/clients", methods=["POST"])
def add_client():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email") or not data.get("phone"):
        return jsonify({"error": "Missing required fields"}), 400

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    db.create_client(name, email, phone)
    return jsonify({"message": "Client added successfully"}), 201

@app.route("/provider", methods=["POST"])
def add_provider():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email") or not data.get("phone") or not data.get("field"):
        return jsonify({"error": "Missing required fields"}), 400

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    field = data.get("field")
    db.create_provider(name, email, phone, field)
    return jsonify({"message": "Provider added successfully"}), 201

@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("description") or not data.get("price") or not data.get("stock"):
        return jsonify({"error": "Missing required fields"}), 400

    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")
    db.create_product(name, description, price, stock)
    return jsonify({"message": "Product added succesfully"}), 201

@app.route("/sales", methods=["POST"])
def add_sale():
    data = request.get_json()

    if not data or not data.get("product_id") or not data.get("employee_id") or not data.get("client_id") or not data.get("date"):
        return jsonify({"error": "Missing required fields"}), 400

    product_id = data.get("product_id")
    employee_id = data.get("employee_id")
    client_id = data.get("client_id")
    date = data.get("date")
    total = data.get("total")
    db.create_sale(client_id, product_id, employee_id, date, total)
    return jsonify({"message": "Sale added succesfully"}), 201

@app.route("/purchases", methods=["POST"])
def add_purchase():
    data = request.get_json()

    if not data or not data.get("product_id") or not data.get("provider_id") or not data.get("employee_id") or not data.get("quantity") or not data.get("total_cost"):
        return jsonify({"error": "Missing required fields"}), 400

    product_id = data.get("product_id")
    provider_id = data.get("provider_id")
    employee_id = data.get("employee_id")
    quantity = data.get("quantity")
    total_cost = data.get("total_cost")
    db.create_purchase(product_id, provider_id, employee_id, quantity, total_cost)
    return jsonify({"message": "Purchase added succesfully"}), 201

@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    
    employee = db.get_employee(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    
    db.delete_employee(employee_id)
    return jsonify({"message": "Employee deleted successfully"}), 200

@app.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):

    client = db.get_client(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    
    db.delete_client(client_id)
    return jsonify({"message": "Client deleted successfully"}), 200

@app.route("/proficers/<int:provider_id>", methods=["DELETE"])
def delete_provider(provider_id):

    provider = db.get_provider(provider_id)
    if not provider:
        return jsonify({"error": "Provider not found"}), 404
    
    db.delete_provider(provider_id)
    return jsonify({"message": "Provider deleted successfully"}), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    product = db.get_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    db.delete_product(product_id)
    return jsonify({"message": "Product deleted successfully"}), 200

@app.route("/sales/<int:sale_id>", methods=["DELETE"])
def delete_sale(sale_id):

    sale = db.get_sale(sale_id)
    if not sale:
        return jsonify({"error": "Sale not found"}), 404
    
    db.delete_sale(sale_id)
    return jsonify({"message": "Sale deleted successfully"}), 200

@app.route("/purchases/<int:purchase_id>", methods=["DELETE"])
def delete_purchase(purchase_id):

    purchase = db.get_purchase(purchase_id)
    if not purchase:
        return jsonify({"error": "Purchase not found"}), 404
    
    db.delete_purchase(purchase_id)
    return jsonify({"message": "Purchase deleted successfully"}), 200


@app.route("/")
if __name__ == '__main__':
    app.run(debug=True)