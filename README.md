# Task tracker
## Introduction

This is the backend part of the Task Tracker project, which is responsible for handling server-side logic and communication with the database. This backend is built using the Django web framework, and uses Django REST framework to provide a RESTful API for the frontend to consume.

## Requirements

To run this backend, you will need to have the following installed on your system:

   * Python 3.x
   * Django 3.x
   * Django REST framework
   * This DB

## Getting Started
pass

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
