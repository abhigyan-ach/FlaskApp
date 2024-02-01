# flaskapp.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity (replace with a database in production)
users = []

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')

    # Store the data in the in-memory list (replace with database storage)
    user_data = {'username': username, 'firstname': firstname, 'lastname': lastname, 'email': email}
    users.append(user_data)

    return redirect(url_for('display_info', username=username))

@app.route('/display-info/<username>')
def display_info(username):
    # Retrieve data from the in-memory list (replace with database retrieval)
    user_data = next((user for user in users if user['username'] == username), None)

    if user_data:
        return render_template('display_info.html', user_data=user_data)
    else:
        return "User not found."

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/retrieve-info', methods=['POST'])
def retrieve_info():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check credentials (you should validate against hashed passwords in a real scenario)
    # For simplicity, this example just checks for the presence of the user in the in-memory list
    user_data = next((user for user in users if user['username'] == username), None)

    if user_data:
        return redirect(url_for('display_info', username=username))
    else:
        return "Invalid credentials."

if __name__ == '__main__':
    app.run(debug=True)
