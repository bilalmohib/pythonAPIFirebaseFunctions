import uuid
from flask import Blueprint, request, jsonify, current_app
from firebase_admin import firestore
from datetime import datetime, timedelta
import pyrebase

config = {
  "apiKey": "AIzaSyCswKTdGAIb3gqvsSMig2pdhDZtYOUMpKs",
  "authDomain": "pythonapi-c0178.firebaseapp.com",
  "databaseURL": "https://pythonapi-c0178-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "pythonapi-c0178",
  "storageBucket": "pythonapi-c0178.appspot.com",
  "messagingSenderId": "397394086527",
  "appId": "1:397394086527:web:7b2c30ff2e0846c386cd4a",
  "measurementId": "G-YLME5TENZK"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firestore.client()
user_Ref = db.collection('user')

userAPI = Blueprint('userAPI', __name__)

# Authentication middleware
def authenticate_user(token):
    try:
        user = auth.get_account_info(token)["users"][0]
        
        if not user:
            return False, "Invalid token"
        user = user

        print("User Info: ", user["email"], user["emailVerified"], user["disabled"])

        # if not user["emailVerified"]:
        #     return False, "Email not verified"
        if not user["disabled"]:
            return True, user
        return False, "User is disabled"
    except Exception as e:
        return False, str(e)

@userAPI.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')

    try:
        user = auth.create_user(email=email, password=password)
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@userAPI.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        user = auth.sign_in_with_email_and_password(email, password)

        # Perform your own password validation here if needed

        # Generate and return an access token
        user_id_token = auth.get_account_info(user['idToken'])
        
        return jsonify({"access_token": user}), 200
    except Exception as e:
        return jsonify({"error": f"An Error Occurred: {e}"}), 401

@userAPI.route('/todo', methods=['GET'])
def get_todos():
    token = request.headers.get('Authorization')

    # Split the token string by space and take the second part
    barrier_token = token.split(" ")[1]

    authenticated, user = authenticate_user(barrier_token)

    if authenticated:
        todos_ref = db.collection('todos').where('email', '==', user["email"]).stream()
        todos = [{**todo.to_dict(), "id": todo.id} for todo in todos_ref]
        return jsonify({'todos': todos}), 200
    return jsonify({'message': user}), 401

@userAPI.route('/todo', methods=['POST'])
def add_todo():
    token = request.headers.get('Authorization')

    # Split the token string by space and take the second part
    barrier_token = token.split(" ")[1]

    authenticated, user = authenticate_user(barrier_token)
    if authenticated:
        data = request.json
        data['email'] = user["email"]
        todo_ref = db.collection('todos').document()
        todo_ref.set(data)
        return jsonify({'message': 'Todo added successfully'}), 200
    return jsonify({'message': user}), 401

@userAPI.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    token = request.headers.get('Authorization')

    # Split the token string by space and take the second part
    barrier_token = token.split(" ")[1]

    authenticated, _ = authenticate_user(barrier_token)
    if authenticated:
        db.collection('todos').document(todo_id).delete()
        return jsonify({'message': 'Todo deleted successfully'}), 200
    return jsonify({'message': 'Unauthorized'}), 401

@userAPI.route('/todo/<todo_id>', methods=['GET'])
def get_todo(todo_id):
    token = request.headers.get('Authorization')

    # Split the token string by space and take the second part
    barrier_token = token.split(" ")[1]

    authenticated, _ = authenticate_user(barrier_token)
    if authenticated:
        todo_ref = db.collection('todos').document(todo_id).get()
        if todo_ref.exists:
            return jsonify(todo_ref.to_dict()), 200
        return jsonify({'message': 'Todo not found'}), 404
    return jsonify({'message': 'Unauthorized'}), 401

