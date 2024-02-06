# from flask import Flask, render_template
# import os

# app = Flask(__name__)
# port = int(os.environ.get("PORT", 8080))

# @app.route('/')
# def index():
#     data = {
#         'title': 'sample data',
#         'content': 'This is some placeholder content for the sample data.'
#     }
#     return data
#     # return render_template('index.html')
#     # return "Hello World"
# @app.route('/second_page')
# def second_page():
#     # Placeholder data
#     data = {
#         'title': 'Second Page',
#         'content': 'This is some placeholder content for the second page.'
#     }
#     return render_template('second_page.html', data=data)
# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0', port=port)



# from flask import Flask, request, jsonify
# import os
# # from google.cloud import firestore
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Initialize Flask app
# app = Flask(__name__)
# port = int(os.environ.get("PORT", 8080))

# # Initialize Firebase
# cred = credentials.Certificate("E:/api/cloudfunctions/sdk-key.json")
# firebase_admin.initialize_app(cred)

# # Firestore client
# db = firestore.client()

# # Initialize Firestore
# db = firestore.Client()

# @app.route('/test_firebase')
# def test_firebase():
#     # Access Firestore
#     data = {
#         'message': 'Firebase integration successful!'
#     }
#     return jsonify(data)


# # # Create a new document in Firestore
# # def create_document(data):
# #     doc_ref = db.collection('api_data').add(data)
# #     return doc_ref.id

# # # Retrieve all documents from Firestore
# # def get_all_documents():
# #     docs = db.collection('api_data').stream()
# #     data = [doc.to_dict() for doc in docs]
# #     return data

# # # Retrieve a specific document from Firestore
# # def get_document(document_id):
# #     doc_ref = db.collection('api_data').document(document_id)
# #     doc = doc_ref.get()
# #     if doc.exists:
# #         return doc.to_dict()
# #     else:
# #         return None

# # # Update a document in Firestore
# # def update_document(document_id, data):
# #     doc_ref = db.collection('api_data').document(document_id)
# #     doc_ref.update(data)

# # # Delete a document from Firestore
# # def delete_document(document_id):
# #     doc_ref = db.collection('api_data').document(document_id)
# #     doc_ref.delete()

# # # Routes for CRUD operations

# # @app.route('/', methods=['GET'])
# # def index():
# #     # Get all documents
# #     data = get_all_documents()
# #     return jsonify(data)

# # @app.route('/create', methods=['POST'])
# # def create():
# #     # Create a new document
# #     data = request.json
# #     document_id = create_document(data)
# #     return jsonify({"message": "Document created successfully", "document_id": document_id})

# # @app.route('/read/<document_id>', methods=['GET'])
# # def read(document_id):
# #     # Retrieve a specific document
# #     data = get_document(document_id)
# #     if data:
# #         return jsonify(data)
# #     else:
# #         return jsonify({"message": "Document not found"}), 404

# # @app.route('/update/<document_id>', methods=['PUT'])
# # def update(document_id):
# #     # Update a document
# #     data = request.json
# #     update_document(document_id, data)
# #     return jsonify({"message": "Document updated successfully"})

# # @app.route('/delete/<document_id>', methods=['DELETE'])
# # def delete(document_id):
# #     # Delete a document
# #     delete_document(document_id)
# #     return jsonify({"message": "Document deleted successfully"})

from flask import Flask, jsonify
import os
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Explicitly provide the full path to the key file
cred = credentials.Certificate("E:/api/cloudfunctions/sdk-key.json")
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
@app.route('/test_firebase')
def test_firebase():
    # Access Firestore
    data = {
        'message': 'Firebase integration successful!'
    }
    return jsonify(data)

port = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
