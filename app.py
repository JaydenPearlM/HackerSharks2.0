from flask import Flask, render_template, request, redirect, url_for, session

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_authenticated(self, password_attempt):
        return self.password == password_attempt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Fake user database (replace with actual user authentication logic)
users = {'john': User('john', 'password123'), 'jane': User('jane', 'pass123')}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username].is_authenticated(password):
        # Valid credentials, store username in session and redirect to home page
        session['username'] = username
        return redirect(url_for('home'))
    else:
        # Invalid credentials, redirect back to login page
        return redirect(url_for('index'))

@app.route('/home')
def home():
    # Retrieve username from session
    username = session.get('username', None)
    if username:
        return render_template('home.html', username=username)
    else:
        # If username not found in session, redirect to login page
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Clear session data, redirect to login page
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
