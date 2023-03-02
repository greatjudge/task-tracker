# API Endpoints:
## 1. Tasks

1. GET /tasks/
    - Returns a list of all tasks

2. POST /tasks/
    - Creates a new task
    - Request Body:
        - `title` (required): Task title
        - `description` (optional): Task description
        - `section` (optional): Task section ID
        - `status` (optional): Task status ID
        - `priority` (optional): Task priority
        - `start_datetime` (required): Start datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
        - `due_datetime` (optional): Due datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
        - `user_id` (optional): User ID assigned to the task.
        - `linked_tasks` (optional): List if task ID that needs to be completed before this task

3. GET /tasks/<task_id>/
    - Returns details of a specific task
    - URL Parameters:
        - `task_id` (required): ID of the task

4. PUT /tasks/<task_id>/
    - Updates an existing task
    - URL Parameters:
        - `task_id` (required)
    - Request Body:
        - `title` (optional): Task title
        - `description` (optional): Task description
        - `section` (optional): Task section ID
        - `status` (optional): Task status ID
        - `priority` (optional): Task priority
        - `start_datetime` (required): Start datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
        - `due_datetime` (optional): Due datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
        - `user_id` (optional): User ID assigned to the task.
        - `linked_tasks` (optional): List if task ID that needs to be completed before this task

5. DELETE /tasks/<task_id>/
    - Deletes a specific task
    - URL Parameters:
        - `task_id` (required): ID of the task


## 2. Task sections

1. GET /sections/
    - Returns a list of all task sections

2. POST /sections/
    - Creates a new task section
    - Request Body:
        - `title` (required): Task section name
        - `color` (optional): Task section color in HEX format

3. GET /sections/<section_id>/
    - Returns details of a specific task section
    - URL Parameters:
        - `section_id` (required): ID of the task section

4. PUT /sections/<section_id>/
    - Updates an existing task section
    - URL Parameters:
        - `section_id` (required): ID of the task section
    - Request Body:
        - `title` (optional): Task section name
        - `color` (optional): Task section color in HEX format

5. DELETE /sections/<section_id>/
    - Deletes a specific task section
    - URL Parameters:
        - `section_id` (required): ID of the task section

6. GET /statuses/
    - Returns a list of all task statuses


## 3. Task status

1. GET /statuses/
    - Returns a list of all task statuses

2. POST /statuses/
    - Creates a new task status
    - Request Body:
        - `title` (required): Task status name

3. GET /statuses/<status_id>/
    - Returns details of a specific task status
    - URL Parameters:
        - `status_id` (required): ID of the task status

4. PUT /statuses/<status_id>/
    - Updates an existing task status
    - URL Parameters:
        - `status_id` (required): ID of the task status
    - Request Body:
        - `title` (optional): Task status name

5. DELETE /statuses/<status_id>/
    - Deletes a specific task status
    - URL Parameters:
        - `status_id` (required): ID of the task status

6. GET /statuses/
    - Returns a list of all task statuses


## 4. Users

1. GET /users/
    - Returns a list of all users

2. GET /users/<user_id>/
    - Returns details of a specific user
    - URL Parameters:
        - `user_id` (required): ID of the user

3. PUT /users/<user_id>/
    - Updates an existing user
    - URL Parameters:
        - `user_id` (required): ID of the user
    - Request Body:
        - 'username` (opt)
        - `first_name` (optional): User first name
        - `last_name` (optional): User last name
        - `email` (optional): User email address

4. DELETE /users/<user_id>/
    - Deletes a specific user
    - URL Parameters:
        - `user_id` (required): ID of the user
