import requests

# Define the URL of the Flask API endpoint
base_url = 'http://127.0.0.1:5000'
update_endpoint = '/students/3'  # Assuming you want to update student with reg_no 1

# Define the student data to update
student_data = {
    "name": "John Lyon",
    "department": "Computer Science",
    "age": 22
}

# Send a PUT request to update the student record
update_url = base_url + update_endpoint
response = requests.put(update_url, json=student_data)

# Print the response content
print(response.text)
