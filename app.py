from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(['Jim', 'James', 'John'])

@app.route('/hello', methods=["GET"])
def get_hello():
    # this is how to extract parameters from query string
    user_name = request.args.get('name')
    message = "hello {}".format(user_name)
    print(message)
    return jsonify({"message": message})

@app.route('/hello', methods=["POST"])
def post_hello():
    # this is how to get the json payload
    json_payload = request.get_json()
    print(json_payload)
    return jsonify({"json_payload": json_payload})

@app.route('/my-website')
def my_website():
    user_name = request.args.get('name')
    return render_template('hello.html', name=user_name)
