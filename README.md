# FastTask-Task-Management-System-using-FastAPI

A simple yet production-style Task Management REST API built using FastAPI, featuring JWT authentication, role-based access control (Admin & Customer), and CRUD operations.

🚀 Features

🔐 JWT Authentication

👥 Role-based access

Admin → view/manage all tasks

Customer → manage only own tasks

🧾 Task CRUD

Create task

View tasks

View task by ID

Update task

Delete task

📚 Swagger UI support

🧩 Clean modular project structure

⚡ FastAPI + OAuth2 standards

🗂️ Project Structure

task-management/

│
├── main.py          # App entry point

├── auth.py          # JWT auth & login logic

├── tasks.py         # Task CRUD routes

├── models.py        # Pydantic models

└── README.md

🛠️ Tech Stack

Python 3.9+

FastAPI

Uvicorn

JWT (python-jose)

OAuth2 Password Flow

Pydantic

📦 Installation

1️⃣ Clone the repository
git clone <your-repo-url>
cd task-management

2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install fastapi uvicorn python-jose

▶️ Running the Application
uvicorn main:app --reload


Server will start at:

http://127.0.0.1:8000

📘 API Documentation (Swagger)

Open in browser:

http://127.0.0.1:8000/docs

🔑 Authentication
Login Endpoint
POST /login

Test Credentials
Username	Password	Role
admin	admin123	Admin
user	user123	Customer
Login Response
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer",
  "role": "admin"
}

🔐 Using JWT Token

Copy access_token

Click Authorize 🔓 in Swagger

Enter:

Bearer <your_token>

📌 API Endpoints
🔹 Tasks (Customer & Admin)
Method	Endpoint	Description
POST	/tasks	Create task
GET	/tasks	Get own tasks
GET	/tasks/{id}	Get task by ID
PUT	/tasks/{id}	Update task
DELETE	/tasks/{id}	Delete task
🔹 Admin Only
Method	Endpoint	Description
GET	/admin/tasks	View all tasks
🧠 Access Rules

Customers can access only their own tasks

Admin can access all tasks

Unauthorized access returns 403 Forbidden

Invalid token returns 401 Unauthorized

⚠️ Important Notes

Task IDs must be passed without quotes in URL

/tasks/uuid-value


This version uses in-memory storage

Restarting server resets data

🔮 Future Enhancements

Database integration (MongoDB / PostgreSQL)

Password hashing (bcrypt)

Refresh tokens

User registration

Pagination & filtering

Deployment (Docker / AWS)

🏁 Conclusion

This project demonstrates:

Real-world JWT authentication

Role-based authorization

Clean FastAPI architecture

Interview-ready backend design

👨‍💻 Author

Syed Owais

AI/ML & Backend Enthusiast

FastAPI • Python • REST APIs
