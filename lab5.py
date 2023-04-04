#importing necessar libraries
from firebase_admin import credentials, firestore
import firebase_admin

#initializing firebase
cred = credentials.Certificate("key.json")
app = firebase_admin.initialize_app(cred)

#creating a firestore client
db = firestore.client()

import json
from flask import Flask, request, jsonify

@functions_framework.http
def main(re):

    if re.path == '/register' and re.method == 'POST':
        return register()

    if re.path == '/get' and re.method == 'GET':
        return get_register()

    else:
        return "invalid"

def register():
    voter = request.get_json()

    student_id = voter['id']

    voters_ref = db.collection('voters')

    new_voter_ref = voters_ref.document(str(student_id))

    query = voters_ref.where("id", "==", str(student_id))

    results = query.get()

    if results:
        return {'error': 'User exists'}

    new_voter_ref.set(voter)

    return voter


def get_register():
    get_voter  = request.args.get('id')
    
    voters_ref = db.collection('voters')
    voter_ref = voters_ref.document(str(get_voter))

    voter = voter_ref.get()

    return jsonify(voter.to_dict())

    
