from groupE_RESTfulAPI import app

# Sample data to import
data_to_import = [
    {'name': 'Vic John', 'department': 'English', 'age': 24},

]

# Import data by calling the add_student function of the Flask API
for student in data_to_import:
    response = app.test_client().post('/students', json=student)
    print(response.get_json())
