
from flask import Flask, jsonify, request #import flask library relevant items from flask model
app = Flask(__name__) #create flask application object

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)#starts the debugger, tracing errors on web page
#