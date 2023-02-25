# Task tracker
## Introduction

This is the backend part of the Task Tracker project, which is responsible for handling server-side logic and communication with the database. This backend is built using the Django web framework, and uses Django REST framework to provide a RESTful API for the frontend to consume.

## Requirements

To run this backend, you will need to have the following installed on your system:

   * Python
   * Django
   * Django REST framework
   * Some DB

## Installation
1. Clone the repository.
2. Navigate to the project directory: `cd task-tracker`.
3. Create a virtual environment: `python3 -m venv env`.
4. Activate the virtual environment: `source env/bin/activate (on Windows: env\Scripts\activate)`.
5. Install the dependencies: `pip install -r requirements.txt`.
6. Run the database migrations: `python manage.py migrate`.

## Usage
To start the server, run the following command: `python manage.py runserver`.  
The server will start running at `http://localhost:8000/`.

## API Endpoints
This backend provides the following API endpoints:
### Task Endpoints
    * GET /tasks: Get all tasks for the current user
    * GET /tasks/:id: Get a specific task by ID
    * POST /tasks: Create a new task
    * PATCH /tasks/:id: Update a specific task by ID
    * DELETE /tasks/:id: Delete a specific task by ID
    
### Reminder Endpoints
    * GET /reminders: Get all reminders for the current user
    * GET /reminders/:id: Get a specific reminder by ID
    * POST /reminders: Create a new reminder
    * PATCH /reminders/:id: Update a specific reminder by ID
    * DELETE /reminders/:id: Delete a specific reminder by ID
Note that these endpoints are just a suggestion and can be modified or expanded based on the specific requirements of the task-tracker project.
