
class Employee:
    """Represents an employee of the company, mostly to log who made a sale or purchased from a provider."""

    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

    def to_dict(self):
        """Converts the Employee instance to a dictionary to use in JSON responses."""
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role
        }    
    
    def validate(self):
        """
        Validates the employee data.
        
        Raises:
            ValueError: If any of the fields are invalid.
        """
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Invalid name")
        if not self.role or not isinstance(self.role, str):
            raise ValueError("Invalid role")    
    
    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', role='{self.role}')"
    
class Client:
    """Represents a client of the company."""

    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
    
    def to_dict(self):
        """Converts the Client instance to a dictionary to use in JSON responses."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }    
    
    def validate(self):
        """
        Validates the client data.

        Raises:
            ValueError: If any of the fields are invalid.
        """
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Invalid name")
        if not self.email or not isinstance(self.email, str) or "@" not in self.email:
            raise ValueError("Invalid email")
        if not self.phone or not isinstance(self.phone, str):
            raise ValueError("Invalid phone")    
    
    def __repr__(self):
        return f"Client(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone}')"
    
class Provider:
    """Represents a provider of the company."""

    def __init__(self, id, name, field):
        self.id = id
        self.name = name
        self.service = field
    
    def to_dict(self):
        """Converts the Provider instance to a dictionary to use in JSON responses."""
        return {
            "id": self.id,
            "name": self.name,
            "service": self.field
        }    
    
    def validate(self):
        """
        Validates the provider data.

        Raises:
            ValueError: If any of the fields are invalid.
        """
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Invalid name")
        if not self.field or not isinstance(self.field, str):
            raise ValueError("Invalid field")    
    
    def __repr__(self):
        return f"Provider(id={self.id}, name='{self.name}', field='{self.field}')"
    
class Product:
    """Represents a product sold by the company."""

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    
    def to_dict(self):
        """Converts the Product instance to a dictionary to use in JSON responses."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }    
    
    def validate(self):
        """
        Validates the product data.

        Raises:
            ValueError: If any of the fields are invalid.
        """
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Invalid name")
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ValueError("Invalid price")
        if not isinstance(self.stock, int) or self.stock < 0:
            raise ValueError("Invalid stock")    
    
    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})"

class Sale:
    """Represents a sale made by the company."""

    def __init__(self, id, product_id, employee_id, client_id, date, total):
        self.id = id
        self.product_id = product_id
        self.employee_id = employee_id
        self.client_id = client_id
        self.date = date
        self.total = total

    def to_dict(self):
        """Converts the Sale instance to a dictionary to use in JSON responses."""
        return {
            "id": self.id,
            "product_id": self.product_id,
            "employee_id": self.employee_id,
            "client_id": self.client_id,
            "date": self.date,
            "total": self.total
        }    
    
    def validate(self):
        """
        Validates the sale data.

        Raises:
            ValueError: If any of the fields are invalid.
        """
        if not isinstance(self.product_id, int) or self.product_id <= 0:
            raise ValueError("Invalid product ID")
        if not isinstance(self.employee_id, int) or self.employee_id <= 0:
            raise ValueError("Invalid employee ID")
        if not isinstance(self.client_id, int) or self.client_id <= 0:
            raise ValueError("Invalid client ID")
        if not isinstance(self.date, int) or self.date <= 0:
            raise ValueError("Invalid date")
        if not isinstance(self.total, (int, float)) or self.total < 0:
            raise ValueError("Invalid total")    
    
    def __repr__(self):
        return f"Sale(id={self.id}, product_id={self.product_id}, employee_id={self.employee_id}, client_id={self.client_id}, date={self.date}, total={self.total})"
    
class Purchase:
    """Represents a purchase made from a provider."""

    def __init__(self, id, product_id, provider_id, employee_id, quantity, total_cost):
        self.id = id
        self.product_id = product_id
        self.provider_id = provider_id
        self.employee_id = employee_id
        self.quantity = quantity
        self.total_cost = total_cost
    
    def to_dict(self):
        """Converts the Purchase instance to a dictionary to use in JSON responses."""
        return {
            "id": self.id,
            "product_id": self.product_id,
            "provider_id": self.provider_id,
            "employee_id": self.employee_id,
            "quantity": self.quantity,
            "total_cost": self.total_cost
        }    
    
    def validate(self):
        """
        Validates the purchase data.

        Raises:
            ValueError: If any of the fields are invalid.
        """
        if not isinstance(self.product_id, int) or self.product_id <= 0:
            raise ValueError("Invalid product ID")
        if not isinstance(self.provider_id, int) or self.provider_id <= 0:
            raise ValueError("Invalid provider ID")
        if not isinstance(self.employee_id, int) or self.employee_id <= 0:
            raise ValueError("Invalid employee ID")
        if not isinstance(self.quantity, int) or self.quantity <= 0:
            raise ValueError("Invalid quantity")
        if not isinstance(self.total_cost, (int, float)) or self.total_cost < 0:
            raise ValueError("Invalid total cost")    
    
    def __repr__(self):
        return f"Purchase(id={self.id}, product_id={self.product_id}, provider_id={self.provider_id}, employee_id={self.employee_id}, quantity={self.quantity}, total_cost={self.total_cost})"