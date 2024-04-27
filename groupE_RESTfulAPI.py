from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Function to create a connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('students.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS students (
                        reg_no INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        department TEXT NOT NULL,
                        age INTEGER NOT NULL)''')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_students_reg_no ON students (reg_no)')
    except sqlite3.Error as e:
        print(e) 
    return conn

# (GET) Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        student = cursor.fetchall()
        conn.close()
        return jsonify({'students': student})
    else:
        return jsonify({'error': 'Database connection error'}), 500

# (GET) Retrieve a specific student by registration number
@app.route('/students/<int:reg_no>', methods=['GET'])
def get_student(reg_no):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE reg_no = ?', (reg_no,))
        student = cursor.fetchone()
        conn.close()
        if student:
            return jsonify({'student': student})
        else:
            return jsonify({'error': 'Student not found'}), 404
    else:
        return jsonify({'error': 'Database connection error'}), 500

# (POST) Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    name = data.get('name')
    department = data.get('department')
    age = data.get('age')
    if name and department and age:
        conn = create_connection()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO students (name, department, age) VALUES (?, ?, ?)', (name, department, age))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Student added successfully'}), 201
    return jsonify({'error': 'Invalid request data'}), 400

# (PUT) Update an existing student by registration number
@app.route('/students/<int:reg_no>', methods=['PUT'])
def update_student(reg_no):
    conn = create_connection()
    if conn is not None:
        data = request.json
        name = data.get('name')
        department = data.get('department')
        age = data.get('age')
        if name and department and age:
            cursor = conn.cursor()
            # Check if the student with the given registration number exists
            cursor.execute('SELECT * FROM students WHERE reg_no = ?', (reg_no,))
            student = cursor.fetchone()
            if student:
                # Update the student information
                cursor.execute('UPDATE students SET name=?, department=?, age=? WHERE reg_no=?',
                               (name, department, age, reg_no))
                conn.commit()
                conn.close()
                return jsonify({'message': 'Student updated successfully'}), 200
            else:
                return jsonify({'error': 'Student not found'}), 404
        else:
            return jsonify({'error': 'Invalid request data'}), 400
    else:
        return jsonify({'error': 'Database connection error'}), 500

@app.route('/students/<int:reg_no>', methods=['DELETE'])
def delete_student(reg_no):
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        # Check if the student with the given registration number exists
        student = cursor.execute('SELECT * FROM students WHERE reg_no = ?', (reg_no,))
        if student is None:
            # If the student does not exist, return a 404 error
            conn.close()
            return jsonify({'error': 'Student not found'}), 404
            
        # If the student exists, delete them from the database
        cursor.execute('DELETE FROM students WHERE reg_no = ?', (reg_no,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Student deleted successfully'})
    else:
        return jsonify({'error': 'Database connection error'}), 500


# Route handler for the root URL
@app.route('/')
def index():
    return '''
    <h1>Welcome to the Student Manager API!</h1>
    <p>This is group_E API project to handle your CRUD operations including:-</p>
    <ul>
        <li>Create Student Records</li>
        <li>Read Student Records</li>
        <li>Update Student Records</li>
        <li>Delete Student Records</li>
    </ul>
    '''

if __name__ == "__main__":
    app.run(debug=True)
