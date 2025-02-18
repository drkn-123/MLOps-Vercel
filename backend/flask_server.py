import os
import flask
import flask_cors
import sys

# create a new flask app
app = flask.Flask(__name__)
flask_cors.CORS(app)


# route to print hellow world
@app.route('/')
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    
