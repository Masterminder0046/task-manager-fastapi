Task Manager (FastAPI)
About the Project

This is a simple task manager application I built using FastAPI. The idea was to understand how a real backend works with authentication, database, and API integration.

Users can create an account, log in, and manage their own tasks. Each user can only see and modify their own data, which is handled using JWT authentication.

The frontend is kept very basic just to test the functionality.

Features
User registration and login
Password hashing (not stored as plain text)
JWT-based authentication
Create, view, update, and delete tasks
Each user has their own tasks (no data overlap)
Basic frontend connected to backend APIs
Tech Stack
Backend: FastAPI
Database: SQLite
Authentication: JWT + Bcrypt
Frontend: HTML, CSS, JavaScript
How to Run Locally

Clone the repository:

git clone <your-repo-link>
cd task_manager

Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app.main:app --reload

Open in browser:

API Docs: http://127.0.0.1:8000/docs
Frontend: open frontend/index.html
Project Structure
app/
  ├── main.py
  ├── models/
  ├── routes/
  ├── schemas/
  ├── utils/

frontend/
  └── index.html
What I Learned

While building this project, I understood:

How APIs are structured using FastAPI
How authentication works using JWT
Why password hashing is important
How frontend and backend communicate
Handling real errors like CORS and dependency issues
Challenges Faced
Setting up JWT authentication correctly
Handling CORS between frontend and backend
Debugging bcrypt hashing issues
Managing proper folder structure and imports
Future Improvements
Better UI (React or modern frontend)
Add pagination and filtering
Deploy with proper domain
Add user roles (admin / normal user)
Author

Sheik
Full Stack Developer (Learning & Building 🚀)
