from src.database import create_database, create_employee, create_client, create_provider, create_product, create_sale, create_purchase

def init_with_sample_data():
    """Initializes the database and populates it with sample data."""
    
    print("Creating database tables...")
    create_database()
    
    print("Adding sample employees...")
    create_employee("Juan Pérez", "Manager")
    create_employee("María García", "Sales Representative")
    create_employee("Carlos López", "Warehouse Assistant")
    
    print("Adding sample clients...")
    create_client("Tech Solutions SA", "contact@techsolutions.com", "+598 2123 4567")
    create_client("Retail Store", "info@retailstore.com", "+598 2234 5678")
    create_client("Office Supplies Co", "orders@officesupplies.com", "+598 2345 6789")
    
    print("Adding sample providers...")
    create_provider("Electronics Wholesale", "sales@electrowholesale.com", "+598 2456 7890", "Electronics")
    create_provider("Office Equipment Inc", "info@officeequip.com", "+598 2567 8901", "Office Supplies")
    create_provider("Tech Imports", "contact@techimports.com", "+598 2678 9012", "Technology")
    
    print("Adding sample products...")
    create_product("Laptop Dell Inspiron", "15.6 inch, 8GB RAM, 256GB SSD", 850.00, 15, 1)
    create_product("Wireless Mouse", "Logitech M185, 2.4GHz", 25.00, 50, 1)
    create_product("Office Chair", "Ergonomic, adjustable height", 180.00, 20, 2)
    create_product("USB-C Cable", "2 meter, fast charging", 12.00, 100, 3)
    create_product("Monitor 24 inch", "Full HD, IPS panel", 220.00, 30, 1)
    
    print("Adding sample sales...")
    create_sale(1, 1, 1, "2025-12-20", 850.00)
    create_sale(2, 2, 2, "2025-12-21", 50.00)
    create_sale(1, 3, 1, "2025-12-21", 360.00)
    create_sale(3, 4, 2, "2025-12-22", 36.00)
    
    print("Adding sample purchases...")
    create_purchase(1, 1, 3, 10, 7500.00)
    create_purchase(2, 1, 3, 50, 1000.00)
    create_purchase(5, 1, 3, 20, 4000.00)
    
    print("\n✅ Database initialized successfully with sample data!")
    print("You can now run your API with: python api.py")

if __name__ == '__main__':
    init_with_sample_data()