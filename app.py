from flask import Flask

from flask_pymongo import MongoClient
from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId 

from flask import jsonify, request 

from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"

mongo = PyMongo(app)


# using /add route using method post to send or add this new user in to the database

@app.route("/add", methods=['POST'])
def create_user():
    _json = request.json
    _id = _json['id']
    _first_name = _json['first_name']
    _email = _json['email']
    _last_name = _json['last_name']
    _company_name = _json['company_name']
    _city = _json['city']
    _state = _json['state']
    _web = _json['web']
    _age = _json['age']
    _zip = _json['zip']

        
    if _id and _zip and _first_name and _email and _last_name and _company_name and _company_name and _city and _state and _zip and _web and request.method == 'POST':
            id = mongo.db.user.insert_one({'id':_id, 'zip': _zip, 'name': _first_name, 'last_name': _last_name, 'company_name': _company_name, 'city': _city, 'state': _state, 'web': _web, 'age': _age}) 
           
            resp = jsonify("User added successfully")

            resp.status_code = 200 

            return resp


    else:
            return not_found() 

# using this /users we are listing all user data 
@app.route("/users")
def users():
    users = mongo.db.user.find()
    resp = dumps(users)

    return resp
    
# using particular user id we can their data
@app.route('/user/<id>')
def  user(id):
     user = mongo.db.user.find_one({'_id':ObjectId(id)})
     resp = dumps(user)
     return resp

# using this /delete/id we are delete particular use from the database using delete method

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    mongo.db.user.delete_one({'_id':ObjectId(id)})
    resp = jsonify("User Deleted Successfully")
    resp.status_code = 200
    return resp 

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):

    _json = request.json
    _id = id
    _first_name = 'first_name'
    _email = 'email'
    _last_name = 'last_name'
    _company_name = 'company_name'
    _city = 'city'
    _state = 'state'
    _web = 'web'
    _age = 'age'
    _zip = 'zip'

        
    if _id and _zip and _first_name and _email and _last_name and _company_name and _company_name and _city and _state and _zip and _web and request.method == 'PUT':
            mongo.db.user.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set':  {'id':_id, 'zip': _zip, 'name': _first_name, 'last_name': _last_name, 'company_name': _company_name, 'city': _city, 'state': _state, 'web': _web, 'age': _age}}) 
           
            resp = jsonify("User updated successfully")

            resp.status_code = 200 

            return resp


    else:
            return not_found() 




     
@app.errorhandler(404)

def not_found(error=None):

        
    message = {

        'status': 404,
        'message': 'Not Found' + request.url 

    }


    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(debug=True)




