from flask import Flask, jsonify, request #import flask library relevant items from flask model
app = Flask(__name__)

languages =[{'name': 'Javascript'}, {'name' :'Python'}, {'name':'Ruby'}]

app.route('/lang',methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language ['name'] == name]
    return jsonify({'language' : [0]}) #running the app in debug mode

app.route('/lang',methods=['POST'])
def addOne():
    language = {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages': language})

app.route('/lang/<string: name>',methods=['PUT'])
def editOne():
    langs = [language for language in languages if language ['name'] == name]
    langs[0]['name']=request.json['name']
    return jsonify({'languages': langs [0]})

app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    langs = [language for language in languages if language ['name'] == name]
    languages.remove(langs[0])
    return jsonify({'language' : language}) 

if __name__=='__main__':
     app.run(debug=True)

    