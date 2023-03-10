# Task tracker
## Introduction

This is the backend part of the Task Tracker project, which is responsible for handling server-side logic and communication with the database. This backend is built using the Django web framework, and uses Django REST framework to provide a RESTful API for the frontend to consume.

## Requirements

To run this backend, you will need to have the following installed on your system:

   * Python
   * Django
   * Django REST framework
   * Postgres

## Installation
1. Clone the repository.
2. Navigate to the project directory: `cd task-tracker`.
3. Create a virtual environment: `python3 -m venv env`.
4. Activate the virtual environment: `source env/bin/activate (on Windows: env\Scripts\activate)`.
5. Install the dependencies: `pip install -r requirements.txt`.
6. Dont remember to set django secter key. You can create the file .env in the same folder with settings.py and write to it `DJANGO_SECRET_KEY`="...(this key)...".
8. Run the database migrations: `python manage.py migrate`.

Or you can use `docker-compose.yml`

## Usage
To start the server, run the following command: `python manage.py runserver`.  
The server will start running at `http://localhost:8000/`.

## API Endpoints
This backend provides the following API endpoints:
### Task Endpoints
    * GET api/tasks: Get all tasks for the current user
    * GET api/tasks/:id: Get a specific task by ID
    * POST api/tasks: Create a new task
    * PUT api/tasks/:id: Update a specific task by ID
    * PATCH api/tasks/:id: Partial update a specific task by ID
    * DELETE api/tasks/:id: Delete a specific task by ID

### Task Section Endpoints
    * GET api/sections: Get all sections for the current user
    * GET api/sections/:id: Get a specific section by ID
    * POST api/sections: Create a new section
    * PUT api/sections/:id: Update a specific section by ID
    * PATCH api/sections/:id: Partial update a specific section by ID
    * DELETE api/sections/:id: Delete a specific section by ID
    
### Task Status Endpoints
    * GET api/statuses: Get all statuses for the current user
    * GET api/statuses/:id: Get a specific status by ID
    * POST api/statuses: Create a new status
    * PATCH api/statuses/:id: Partial update a specific status by ID
    * PUT api/statuses/:id: Update a specific status by ID
    * DELETE api/statuses/:id: Delete a specific status by ID

### User Endpoints
    * GET /users/<user_id>/: Returns details of a specific user
    * PUT /users/<user_id>/: Update an existing user
    * PATCH /users/<user_id>/: Partial update an existing user
    * PUT /users/<user_id>/: Change password an existing user
    * POST /users/register/: Register user
    * POST /token/: auth user and get access and refresh tokens
    * POST /token/refresh: get access token



