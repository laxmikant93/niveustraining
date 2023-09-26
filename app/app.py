from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity (you should use a database in a production environment)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Get form data
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Store the user data (in-memory for simplicity)
    users.append({'username': username, 'email': email, 'password': password})

    # Redirect to a success page or do further processing
    return "Registration successful! You can log in now."

if __name__ == '__main__':
    app.run(host='0.0.0.0')
