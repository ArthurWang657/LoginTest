import flask
from flask import render_template, request
app = flask.Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('LoginPage.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    print("post : email => ", email)
    username = request.form['username']
    print("post : username => ", username)
    password = request.form['password']
    print("post : password => ", password)
    
    return render_template('ResultPage.html')

if __name__ == '__main__':
    app.debug = True
    app.run()