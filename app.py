from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'replace_with_secret_key'  # Needed for session handling

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.form['name']
    email = request.form['email']
    plan = request.form['plan']

    conn = get_db_connection()
    conn.execute('INSERT INTO users (name, email, subscription_type) VALUES (?, ?, ?)',
                 (name, email, plan))
    conn.commit()
    conn.close()
    return redirect('/')

# --- Admin login route ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple hardcoded admin check (you can upgrade to a table later)
        if username == 'admin' and password == 'password123':
            session['admin'] = True
            return redirect('/admin')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

@app.route('/admin')
def admin():
    # Only allow access if admin logged in
    if not session.get('admin'):
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('admin.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)