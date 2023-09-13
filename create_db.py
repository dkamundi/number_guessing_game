import sqlite3
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

def create_db():
    con=sqlite3.connect(database=r"ngg.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(uid INTEGER PRIMARY KEY AUTOINCREMENT,username text, email text, password text, created_at DATETIME DEFAULT CURRENT_TIMESTAMP )")
    con.commit()
create_db()

@app.route
def index():
    # Your code to fetch data from the database and render a template
    return render_template("index.html")

@app.route('/loigin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        conn = sqlite3.connect('ngg.db')
        cursor = conn.cursor()

        # Retrieve the user data based of the entered username
        cursor.execute("SELECT id, username, password, FROM users WHERE username=?", (username))
        user_data = cursor.fetchone()

        # Close the database connection
        conn.close()

    if user_data:
        # User found, verify the password
        user_id, stored_username, hashed_password = user_data

        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            # Password is correct, set user session and redirect to the dashboard
            session['user_id'] = user_id
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            # Password is incorrect, show an error message
            flash('Incorrect password. Please try again.','danger')
    else:
        # Username not in the system, show an error message
        flash('Username not found. Please register or try a different username.', 'danger')
    
    # Render the login form
    return render_template('login.html')


# Function to securely hash the password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration form submission
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already in use
        conn = sqlite3.connect('ngg.db')
        cursor = conn.cursor()

        cursor.excecute("SELECT username FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            # Redirect to registration with an error message or handle the error
            return "Username already exists. Please choose another."
        
        # Securely hash the password
        hashed_password = hash_password(password)

        # Insert data into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()

        # After successful registration, redirect to the login page
        return redirect(url_for('login'))
    
    # Render the registration form
    return render_template('register.html')







if __name__ == "__main__":
    app.run(debug=True)

