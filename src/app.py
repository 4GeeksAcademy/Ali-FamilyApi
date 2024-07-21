"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
jackson_family = FamilyStructure("Jackson")  # Create the jackson family object


@app.route('/members', methods=['GET', 'POST'])
def handle_all_members():
    response_body = {}
    if request.method == 'GET':
        members = jackson_family.get_all_members()
        response_body["results"]= members
        return jsonify(response_body), 200
        
    if request.method == 'POST':
        data = request.json
        if data:
            jackson_family.add_member(data)
            response_body["message"] = "Member added"
            response_body["results"] = jackson_family.get_all_members()[-1]
            return jsonify(response_body), 200
        else:
            response_body["message"] = "Invalid data"
            return jsonify(response_body), 400
        
        
@app.route('/members/<int:member_id>', methods=['GET', 'DELETE'])
def handle_single_member(member_id):
    response_body = {}
    if request.method == 'GET':
        member = jackson_family.get_member(member_id)
        if member:
            return jsonify(member), 200
        else:
            response_body["message"] = "Member doesn't exist"
            return jsonify(response_body), 404
    
    if request.method == 'PUT':
        member[member_id] = request.json
        response_body['message'] = f'Member {member_id} edited'
        response_body['results'] = member[member_id]
        return response_body, 200

    if request.method == 'DELETE':
        jackson_family.delete_member(member_id)
        response_body = {"message": "Member deleted"}
        return jsonify(response_body), 200


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"hello": "world", 
                     "family": members}
    return jsonify(response_body), 200


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
