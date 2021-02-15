from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(['Jim', 'James', 'John'])

@app.route('/hello', methods=["GET", "POST"])
def hello():
    return jsonify(['Jim', 'James', 'John'])


@app.route('/my-website')
def my_website():
    return render_template('hello.html', name="Antonio")
