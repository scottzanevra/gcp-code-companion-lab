

def multiply(x,y):
    try:
        return x*y
    except TypeError:
        print('Invalid input types')
    except ValueError:
        print('Invalid input values')
    except Exception as e:
        print('Error multiplying numbers:', e)




def create_server_connection(host_name, user_name, user_password):
    try:
        return mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password)
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


