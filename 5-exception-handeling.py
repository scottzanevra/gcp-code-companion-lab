
# ************************** Code Companion Prompt ***********************************
# Write some exception handeling

def multiply(x,y):
    return x*y




def create_server_connection(host_name, user_name, user_password):
    return mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password)