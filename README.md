# FastTask-Task-Management-System-using-FastAPI

A simple Task Management REST API built using FastAPI, implementing full CRUD operations (Create, Read, Update, Delete).
This project is designed for learning REST APIs, FastAPI fundamentals, and Swagger UI.

📌 Features

Create, read, update, and delete tasks

RESTful API design

Input validation using Pydantic

Auto-generated Swagger UI documentation

Lightweight and easy to understand

🛠️ Tech Stack

Python 3.8+

FastAPI

Uvicorn

Pydantic

📂 Project Structure
task-management-system/
├── main.py
└── README.md

▶️ Getting Started
1️⃣ Clone the repository
git clone https://github.com/your-username/task-management-system.git
cd task-management-system

2️⃣ Install dependencies
pip install fastapi uvicorn

3️⃣ Run the application
uvicorn main:app --reload

4️⃣ Open in browser

API base URL

http://localhost:8000


Swagger UI

http://localhost:8000/docs

📡 API Endpoints
Method	Endpoint	Description
POST	/tasks	Create a new task
GET	/tasks	Retrieve all tasks
GET	/tasks/{task_id}	Retrieve a task by ID
PUT	/tasks/{task_id}	Update an existing task
DELETE	/tasks/{task_id}	Delete a task
🧪 Example Request
Create a Task

POST /tasks

{
  "title": "Learn FastAPI",
  "description": "Build REST API",
  "completed": false
}


Response

{
  "id": "c8f9a2a1-5d4c-4d1b-a3e5-123456789abc",
  "title": "Learn FastAPI",
  "description": "Build REST API",
  "completed": false
}

⚠️ Notes

Uses an in-memory data store

Data resets on server restart

Intended for learning and prototyping

🚧 Future Enhancements

Database integration (SQLite / MongoDB)

JWT authentication

Pagination and filtering

Frontend integration (React)

👤 Author

Syed Owais Mohiuddin
📄 License

This project is licensed under the MIT License.

📄 License

This project is licensed under the MIT License.
