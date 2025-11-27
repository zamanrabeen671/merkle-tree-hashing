# Merkle Tree File Integrity System

A FastAPI application to securely upload files, verify their integrity using Merkle Trees, and optionally support one-time secure file sharing.

## Features

- File upload with Merkle Tree hash generation
- File integrity verification
- PostgreSQL integration
- JWT authentication for protected routes
- Optional one-time download tokens
- FastAPI Swagger UI for testing endpoints

---

## Requirements

- Python 3.10+
- PostgreSQL
- pip

---

## Setup

1. **Clone the repository**

```bash
git clone <repo-url>
cd <repo-folder>

2. **Create a virtual environment

Windows

python -m venv venv
venv\Scripts\activate


Mac/Linux

python3 -m venv venv
source venv/bin/activate


3. **Install dependencies

pip install -r requirements.txt


4. **Configure environment variables

Create a .env file in the project root:

DATABASE_URL=postgresql://username:password@localhost:5432/merkle_db
SECRET_KEY=your_secret_key


5. **Set up PostgreSQL database

6. **CREATE DATABASE merkle_db;


Create tables

python create_tables.py


Tables for files, users, and optional download_tokens will be created.

Run the Application
uvicorn app.main:app --reload


Open Swagger UI: http://127.0.0.1:8000/docs

Endpoints
Auth

POST /auth/register → register a new user

POST /auth/login → login and get JWT token

Files

POST /files/upload → upload a file (protected route)

POST /files/verify/{file_id} → verify file integrity

GET /files/download?token=<token> → optional one-time download

Notes

.env file should never be committed — it contains sensitive info.

Uploaded files can be stored locally (uploads/) or in cloud storage.

JWT token is required for protected routes.```