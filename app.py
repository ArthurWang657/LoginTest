import flask
from flask import render_template, request, url_for

app = flask.Flask(__name__, static_folder='public', static_url_path="/")

@app.route("/")
@app.route("/home")
def home():
    return render_template('LoginPage.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    print("post : email => ", email)
    tax_id = request.form['tax_id']
    print("post : tax_id => ", tax_id)
    
    
    return render_template('ResultPage.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
