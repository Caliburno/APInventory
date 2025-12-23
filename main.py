from src.database import create_database
from api import main

if __name__ == "__main__":
    create_database()
    main()