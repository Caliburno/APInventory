# APInventory

REST API for inventory management system with full CRUD operations for managing business resources.

## About

API version of CLInventory, demonstrating the conversion of a CLI application into a RESTful web service. This project showcases solid software architecture principles - the same database layer serves both CLI and API interfaces without modification.

## Features

Complete REST API with CRUD operations for:
- **Employees**: Manage staff records
- **Clients**: Track customer information  
- **Providers**: Maintain supplier database
- **Products**: Catalog inventory items with pricing and stock levels
- **Sales**: Record and track transactions

## Architecture

Modular design with clear separation of concerns:

```
APInventory/
├── api.py           # Flask REST API endpoints
├── src/
│   ├── database.py  # Database operations (unchanged from CLInventory)
│   ├── config.py    # Configuration settings
└── requirements.txt # Python dependencies
```

The database layer remains identical to CLInventory, demonstrating that well-architected code can adapt to different interfaces without rewriting business logic.

## Tech Stack

- Python
- Flask (REST API framework)
- SQLite
- VS Code

## API Endpoints

### Employees
- `GET /employees` - List all employees
- `GET /employees/<id>` - Get specific employee
- `POST /employees` - Create new employee
- `PUT /employees/<id>` - Update employee
- `DELETE /employees/<id>` - Delete employee

### Clients
- `GET /clients` - List all clients
- `GET /clients/<id>` - Get specific client
- `POST /clients` - Create new client
- `PUT /clients/<id>` - Update client
- `DELETE /clients/<id>` - Delete client

### Providers
- `GET /providers` - List all providers
- `GET /providers/<id>` - Get specific provider
- `POST /providers` - Create new provider
- `PUT /providers/<id>` - Update provider
- `DELETE /providers/<id>` - Delete provider

### Products
- `GET /products` - List all products
- `GET /products/<id>` - Get specific product
- `POST /products` - Create new product
- `PUT /products/<id>` - Update product
- `DELETE /products/<id>` - Delete product

### Sales
- `GET /sales` - List all sales
- `GET /sales/<id>` - Get specific sale
- `POST /sales` - Create new sale
- `PUT /sales/<id>` - Update sale
- `DELETE /sales/<id>` - Delete sale

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/Caliburno/APInventory.git
cd APInventory
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the API:
```bash
python api.py
```

The API will be available at `http://localhost:5000`

## Testing the API

### Using curl

**Create an employee:**
```bash
curl -X POST http://localhost:5000/employees \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"John Doe\", \"role\": \"Manager\"}"
```

**Get all employees:**
```bash
curl http://localhost:5000/employees
```

**Get specific employee:**
```bash
curl http://localhost:5000/employees/1
```

**Update employee:**
```bash
curl -X PUT http://localhost:5000/employees/1 \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"John Smith\", \"role\": \"Senior Manager\"}"
```

**Delete employee:**
```bash
curl -X DELETE http://localhost:5000/employees/1
```

### Using Postman

1. Import the API into Postman
2. Set base URL to `http://localhost:5000`
3. Test each endpoint with appropriate JSON payloads

**Example JSON payloads:**

Employee:
```json
{
  "name": "Jane Doe",
  "role": "Developer"
}
```

Client:
```json
{
  "name": "Acme Corp",
  "email": "contact@acme.com",
  "phone": "555-0100"
}
```

Product:
```json
{
  "name": "Laptop",
  "description": "Dell XPS 15",
  "price": 1299.99,
  "stock": 50,
  "provider_id": 1
}
```

Sale:
```json
{
  "client_id": 1,
  "product_id": 1,
  "employee_id": 1,
  "date": "2024-12-16",
  "total": 1299.99
}
```

## Status Codes

- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid input data
- `404 Not Found` - Resource not found

## Project Evolution

This project demonstrates the evolution from CLI to API:
1. **CLInventory** - Command-line interface with menu-driven interaction
2. **APInventory** - REST API exposing the same functionality over HTTP

The unchanged database layer proves the value of modular architecture and separation of concerns.

## Purpose

Educational project demonstrating:
- REST API design principles
- Flask framework usage
- HTTP methods and status codes
- JSON request/response handling
- Software architecture and code reusability
- Migration from CLI to web service architecture
