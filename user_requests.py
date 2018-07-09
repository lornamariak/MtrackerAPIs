from flask import Flask, jsonify, request #import flask library relevant items from flask model
app = Flask(__name__)

requests =[]

app.route('/users/requests',methods=['POST'])
def addRequest():
    userRequest = {'Equipment Name': request.json['Equipment Name']}
    requests.append(userRequest)
    return jsonify({'requests': requests})

app.route('/users/requests',methods=['GET'])
def allRequests():
    return jsonify({'requests' : requests})

app.route('/users/requests/<requestId>',methods=['GET'])
def oneRequest():
    requestId = [id for id in requests if id [''] == id]
    return jsonify({'id' : requestId [0]})


app.route('/users/requests/<requestId>',methods=['PUT'])
def editRequest():
    requestId = [id for id in requests if id [''] == id]
    requestId[0]['']=request.json['id']
    return jsonify({'requests': requestId [0]})

if __name__=='__main__':
     app.run(debug=True)