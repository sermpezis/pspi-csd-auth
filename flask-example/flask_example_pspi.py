'''
Required steps for installing and setting up flask
	1) installation (preferrably in a virtualenv):		
			pip install flask
	2) set the FLASK_APP environment variable:		
			export FLASK_APP=flask_example_pspi.py (Linux)
			set FLASK_APP=flask_example_pspi.py (Windows)
	3) run flask:		
			python -m flask run
	4) by default flask runs on http://127.0.0.1:5000/ (or localhost:5000)

'''

'''
This is our "Database" in this example.
'''
LIST_OF_PEOPLE = [{'name':'Bob','gender':'man', 'age':30},\
				  {'name':'Alice','gender':'woman', 'age':40},\
				  {'name':'John','gender':'man', 'age':20},\
				  {'name':'Wanda','gender':'NA', 'age':100}]


from flask import Flask, render_template, jsonify, request
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
	return 'Welcome to our API'

@app.route("/api")
def api_home():
	'''
	You can have any functionality here, e.g., implement logic, call other functions, retrieve data from DB, etc.
	In this example we only define (statically) two values/words we want to appear in the API's home page
	'''
	api_params_values=['man', 'woman']
	return jsonify(api_params_values)
	# return render_template('home.html', title='API home page', our_custom_input=api_params_values)
	# return render_template('home.html', our_custom_input=api_params_values)
	# return render_template('home_extended.html', title='API home page', our_custom_input=api_params_values)


@app.route("/api/genders/<gender_value>")
def get_list_of_people_of_same_gender(gender_value):
	list_of_people_of_same_gender = []
	for p in LIST_OF_PEOPLE:
		if p['gender'] == gender_value:
			list_of_people_of_same_gender.append(p)
	return jsonify(list_of_people_of_same_gender)

@app.route("/api/create", methods=['POST'])
def add_person_to_list_of_people():
	new_person = {}
	new_person['name'] = request.args.get('name')
	new_person['gender'] = request.args.get('gender')
	new_person['age'] = int(request.args.get('age'))
	LIST_OF_PEOPLE.append(new_person)
	return jsonify(new_person)



'''
optionally different IP and ports can be selected
'''
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5001)