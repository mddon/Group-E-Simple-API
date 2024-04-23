from flask import Flask, jsonify

app = Flask(__name__)

tasks = []  # List to store tasks

def get_tasks():
    return jsonify(tasks)

def get_task(index):
    if index < len(tasks):
        return jsonify(tasks[index])
    else:
        return jsonify({'error': 'Task not found'}), 404

def add_task():
    data = request.json
    tasks.append(data)
    return jsonify({'message': 'Task added successfully'}), 201

def update_task(index):
    if index < len(tasks):
        data = request.json
        tasks[index] = data
        return jsonify({'message': 'Task updated successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404

def delete_task(index):
    if index < len(tasks):
        del tasks[index]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404