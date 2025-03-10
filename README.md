# Task Tracker API (FastAPI)

This is a Task Tracker API built with FastAPI.  
It allows you to create, update, retrieve, and delete tasks. 

## Task Model Schema

| Field         | Type      | Description                                        |
|---------------|-----------|---------------------------------------------------|
| `id`          | `int`     | Primary key (auto-generated).                     |
| `title`       | `string`  | Task title.                        |
| `description` | `string`  | Task description (optional).                      |
| `priority`    | `int`     | Task priority (1 = High, 2 = Medium, 3 = Low).    |
| `due_date`    | `datetime`| Due date for the task.                            |
| `completed`   | `bool`    | Completion status (default: `False`).             |  

---

## Running Locally

1. **Create virtual environment**:
   `python3 -m venv taskvenv`
2. **Activate virtual environment**:
    `source taskvenv/bin/activate`
3. **Run app in Docker**:
    `docker-compose up --build`

## Running Tests
To run tests, use:
  `pytest`

## API Documentation
  Interactive API documentation is available at:
    http://0.0.0.0:8010/docs

## Example API Calls
**Get a Task by ID**
curl -X GET http://0.0.0.0:8010/tasks/{id}

**Create a Task**

curl -X POST "http://0.0.0.0:8010/tasks/" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "My New Task",
           "description": "This is a test task",
           "priority": 2,
           "due_date": "2025-03-08T10:00:00"
         }'

**Update a Task (e.g., mark as completed)**
curl -X PUT "http://0.0.0.0:8010/tasks/{id}" \
     -H "Content-Type: application/json" \
     -d '{
           "completed": true
         }'
         
**Delete a Task**
curl -X DELETE http://0.0.0.0:8010/tasks/{id}
