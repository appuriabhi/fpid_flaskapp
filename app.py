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
        expires = datetime.now() + timedelta(days=30*13)
        response = make_response()
        response.set_cookie(cookie_name, cookie_value, expires=expires, secure=False, httponly=True, samesite='Lax', domain='onrender.com')
        return response

@app.route('/')
def home():
    response = make_response(render_template('home.html'))
    return response

@app.route('/about')
def about():
    response = make_response(render_template('about.html'))
    return response

if __name__ == '__main__':
    app.run(debug=True)
