import sqlite3
from flask import Flask, render_template, request, redirect, url_for

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

        # Verify username and password 
        if username == 'example_user' and password == 'password':
            return redirect(url_for('dashboard'))
        
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)

