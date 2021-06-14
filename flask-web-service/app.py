import random
import flask
from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/')
def root():
    return {"message":"Please call GET, POST, PATCH or DELETE on the /user resource."}

# A primitive data model
class User():
    def __init__(self,
                 id: str    = "",
                 name: str  = "",
                 email: str = "",
                 age: int   = None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(cls, json_text):
        return User(**json.loads(json_text))

# A primitive database
_USERS = {}
# _TASKS = {}


# curl -X GET http://localhost:80/user/123
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    id = str(id)
    if id not in _USERS:
        # Return 404 if not found
        return Response('{"error": True, "message":"User does not exist 🤦‍♂️"}', status=404, mimetype='application/json')

    user: User = _USERS[id]
    return user.to_json()

# curl -X POST http://localhost:80/user -H "Content-Type: application/json" --data-raw '{"id": "123", "age": 80, "name": "dick cheney"}'
@app.route('/user', methods=['POST'])
def create_user():
    obj: dict = flask.request.json # receives data-raw value and parses it into a python dictionary
    new_user = User(**obj)
    new_user.id = id = str(random.randint(0, 10000000000))

    # Add new user to database
    _USERS[id] = new_user

    # flask automatically converts dictionaries to json
    return {"id": id, "error": None}, 200

# curl -X PATCH http://localhost:80/user -H "Content-Type: application/json" --data-raw '{"id": "123", "age": 80, "name": "dick cheney"}'
@app.route('/user', methods=['PATCH'])
def update_user():
    obj: dict = flask.request.json # receives data-raw value and parses it into a python dictionary
    user = User(**obj)
    if user.id not in _USERS:
        return {"error": "User already exists."}, 400

    _USERS[obj['id']] = user
    return {"error": None}, 200

# curl -X DELETE http://localhost:80/user/<id>
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    if id not in _USERS.keys():
        # Return 404 if not found
        return Response('{"error": True, "message":"User does not exist 🤦‍♂️"}', status=404, mimetype='application/json')

    del _USERS[str(id)]

    return {"error": None}, 200
