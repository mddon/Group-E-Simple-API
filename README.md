# RESTful Task API

This RESTful API allows users to perform basic CRUD operations (Create, Read, Update, Delete) on a list of tasks.

## Endpoints

### Get All Tasks

GET /tasks

Retrieves a list of all tasks.

### Get Task by ID

GET /tasks/{id}

Retrieves a single task by its unique ID.
                                                  ### Create a Task

POST /tasks
Creates a new task.

### Update a Task

PUT /tasks/{id}
Updates an existing task by its ID.

### Delete a Task

DELETE /tasks/{id}
Deletes a task by its ID.

## Resource Representation

A task object has the following attributes:

- `id` (string): Unique identifier for the task.
- `title` (string): Title of the task.
- `description` (string): Description of the task.
- `completed` (boolean): Indicates whether the tas
k is completed or not.

Example task object:
```json
{
  "id": "1",
  "title": "Complete API documentation",
  "description": "Write documentation for the RESTful API.",
  "completed": false
}

