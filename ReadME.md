📝 Task Manager API (Django + JWT)

A simple Task Manager REST API built using Django REST Framework and JWT Authentication.
Each user can register, login, and manage their own tasks securely.

🚀 Features

🔐 JWT Authentication (Login & Protected APIs)

👤 User Registration

✅ Create, Read, Update, Delete Tasks

🔒 User-specific task access (no cross-user access)

🧪 Easy API testing using Postman

📦 Clean project structure with separate apps

🛠 Tech Stack

Python 3.x

Django

Django REST Framework (DRF)

Simple JWT

SQLite (default)

📁 Project Structure
task_manager/
│
├── accounts/          # User auth (register & login)
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── tasks/             # Task management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── task_manager/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-url>
cd task_manager

2️⃣ Create Virtual Environment
python -m venv env
env\Scripts\activate  # Windows

3️⃣ Install Dependencies
pip install django djangorestframework djangorestframework-simplejwt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start Server
python manage.py runserver


Server will run at:

http://127.0.0.1:8000/

🔐 Authentication APIs
🔹 Register User
POST /api/auth/register/


Body (JSON):

{
  "username": "zeel",
  "password": "1234"
}

🔹 Login User (JWT)
POST /api/auth/login/


Body (JSON):

{
  "username": "zeel",
  "password": "1234"
}


Response:

{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}

🧪 Using JWT in Postman

Copy access token

Go to Authorization tab

Select Bearer Token

Paste access token

✅ Task APIs (Authenticated)
🔹 Create Task
POST /api/tasks/

{
  "title": "Learn Django JWT"
}

🔹 Get All Tasks (User Only)
GET /api/tasks/

🔹 Get Task by ID
GET /api/tasks/{id}/

🔹 Update Task
PUT /api/tasks/{id}/

{
  "title": "Learn JWT deeply",
  "completed": true
}

🔹 Delete Task
DELETE /api/tasks/{id}/

🔒 Security

❌ Anonymous users cannot access tasks

❌ Users cannot access other users' tasks

✅ Tasks are always linked to request.user

🧠 How Task Ownership Works

JWT token identifies the user

Backend uses request.user

Tasks are filtered by logged-in user automatically

🧩 Future Improvements

Refresh token handling

Custom permissions

Swagger / OpenAPI docs

Docker support

Custom User model

Task categories & due dates

👨‍💻 Author

Zeel Gajjar
Backend Developer (Python, Django, FastAPI)