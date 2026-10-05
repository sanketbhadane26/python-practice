# First FastAPI App

This is my first FastAPI project.

The purpose of this project is to understand the basic structure of a FastAPI application, routing, HTTP GET requests, JSON responses, and API testing using Postman.

## Features

- FastAPI application setup
- GET request handling
- Multiple API routes
- JSON responses
- API testing using Postman
- Automatic API documentation

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Postman
- Git
- GitHub

## Project Structure

```text
first-fastapi-app/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── venv/

API Routes
Home
GET /

Response:
{
    "message": "Hello World"
}

About
GET /about

Response:
{
    "message": "This is the About page"
}

Contact
GET /contact

Response:
{
    "message": "This is the Contact page"
}

How to Run
1. Clone the repository
git clone <your-repository-url>

2. Open the project
cd first-fastapi-app

3. Create a virtual environment
python -m venv venv

4. Activate the virtual environment
Windows PowerShell:
.\venv\Scripts\Activate.ps1

5. Install dependencies
pip install -r requirements.txt

6. Start the FastAPI server
uvicorn main:app --reload

The application will run at:
http://127.0.0.1:8000

Testing
The API can be tested using a browser, Postman, or FastAPI's automatic documentation.
FastAPI documentation:
http://127.0.0.1:8000/docs

What I Learned
- What FastAPI is
- How to create a FastAPI application
- How routes work
- How GET requests work
- How Python functions are connected to API endpoints
- How JSON responses work
- What HTTP status codes mean
- How to test APIs using Postman
- How to run a FastAPI application using Uvicorn
- How to use Git and GitHub for version control
Basic Request Flow
Client / Browser / Postman
          ↓
      HTTP Request
          ↓
        FastAPI
          ↓
     Python Function
          ↓
      JSON Response

Future Improvements
- Add POST requests
- Learn request bodies
- Learn Pydantic models
- Add CRUD operations
- Connect FastAPI with PostgreSQL
- Build a backend project
Author
Sanket
This project was created as part of my backend development learning journey.