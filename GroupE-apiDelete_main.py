from groupE_RESTfulAPI import app
#import requests

# Define the sample data to import (student details)
data_to_import = [
    {'reg_no': 6},
   # {'reg_no': 8},
   # {'reg_no': 9}
]

""" # Base URL of the Flask API
base_url = 'http://127.0.0.1:5000'

# Endpoint for deleting a student
delete_endpoint = '/students/'

# List of response messages
response_messages = []

# Iterate over each student data and send DELETE requests
for student in data_to_import:
    # Get the registration number (reg_no) of the student
    reg_no = student['reg_no']
    
    # Construct the URL for the DELETE request
    delete_url = base_url + delete_endpoint + str(reg_no)
    
    # Send the DELETE request
    response = requests.delete(delete_url)
    
    # Append the response message to the list
    response_messages.append(response.json()) """

# Print the response messages
for message in data_to_import:
    print(message)
