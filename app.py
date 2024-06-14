from flask import Flask, render_template, request, make_response
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

@app.before_request
def before_request():
    cookie_name = 'FPID'
    cookie_value = request.cookies.get(cookie_name)

    if not cookie_value:
        cookie_value = str(uuid.uuid4())

    expires = datetime.now()
    expires = expires + timedelta(days=30*13)
    response = make_response()
    response.set_cookie(cookie_name, cookie_value, expires=expires, secure=False, httponly=True, samesite='Lax', domain='fpid-flaskapp.onrender.com')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)