from database import get_connection

def test_database_connection():
    """
    Test the PostgreSQL/PostGIS database connection.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT version();")
        result = cursor.fetchone()

        print("\n===================================")
        print("DATABASE CONNECTION SUCCESSFUL")
        print("===================================")
        print("\nPostgreSQL Version:")
        print(result[0])

        cursor.close()
        connection.close()

        print("\nConnection closed successfully.")

    except Exception as error:
        print("\n===================================")
        print("DATABASE CONNECTION FAILED")
        print("===================================")
        print("\nError:")
        print(error)

if __name__ == "__main__":
    test_database_connection()