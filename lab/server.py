# Import the Flask class from the flask module
from flask import Flask, jsonify, make_response, request
from data import data

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

@app.route("/")
def index():
	return "hello world"


@app.route("/no_content")
def no_content():
	return ({"message:": "No Content found"}, 204)

@app.route("/exp")
def index_explicit():
	resp = make_response({"message": "Hello world"})
	resp.status_code = 200
	return resp

@app.route("/data")
def get_data():
	try:
		if data and len(data) > 0:
			return {"message": f"Data of length {len(data)} found"}
		else:
			return {"message": "Data is empty"}, 500
	except NameError:
		return {"message": "Data not found"}, 404
	
@app.route("/name_search")
def name_search():
	query = request.args.get('q')
	if not query:
		return {"message": "Query parameter 'q' is missing"}, 422
	
	for person in data:
		if query.lower() in person["first_name"].lower():
			return person
		
	return {"message": "Person not found"}, 404

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
	for person in data:
		if person["id"] == str(id):
			return person
		
	return {"message": "Person not found"}, 404

@app.route("/person/<uuid:id>", methods=["DELETE"])
def delete_by_uuid(id):
	for person in data:
		if person["id"] == str(id):
			data.remove(person)
			return {"message": f"Person with ID {id} deleteed"}, 200
	
	return {"message": "Person not found"}, 404

@app.route("/person", methods=["POST"])
def add_by_uuid():
	new_person = request.json
	if not new_person:
		return {"message": "Invalid input parameter"}, 422
	
	try:
		data.append(new_person)
	except NameError:
		return {"message": "data not defined"}, 500
	
	return {"message" : f"{new_person['id']}"}, 200

@app.errorhandler(404)
def api_not_found(error):
	return {"message": "API not found"}, 404