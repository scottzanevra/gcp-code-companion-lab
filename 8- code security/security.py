

# ************************** Code Companion Prompt ***********************************
# What security vunrabilities exist, how could this be improved
def get_user(user_input):
    user_input = input("Enter your username: ")
    query = "SELECT * FROM users WHERE username = '" + user_input + "';"
    result = execute_query(query) 
    return result



# ************************** Code Companion Prompt ***********************************
# What security vunrabilities exist, how could this be improved
user_input = input("Enter filename: ")
with open(user_input, 'r') as file:  
    content = file.read()



# ************************** Code Companion Prompt ***********************************
# What security vunrabilities exist, how could this be improved
import os
directory = input("Enter the directory to list: ")
command = f"ls {directory}"  # Vulnerable to Command Injection
os.system(command)



# ************************** Code Companion Prompt ***********************************
# What security vunrabilities exist, how could this be improved
import pickle
serialized_data = input("Enter serialized data: ")
deserialized_data = pickle.loads(serialized_data.encode('latin1'))



# ************************** Code Companion Prompt ***********************************
# What security vunrabilities exist, how could this be improved
@app.route('/search')
def search():
    query = request.args.get('q')
    return f"<p>Search results for: {query}</p>" 