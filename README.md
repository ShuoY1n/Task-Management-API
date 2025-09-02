# Task Management API

A REST API project that provides user authentication and task management capabilities using FastAPI, SQLAlchemy, and JWT tokens.

## What it does

- Provides user registration and login with secure password hashing
- Allows users to create, read, update, and delete tasks
- Manages task statuses (incomplete, in progress, completed)
- Filters tasks by status or due date
- Secures all endpoints with JWT-based authentication
- Stores data in a PostgreSQL database using SQLAlchemy ORM

## Motivation

I wanted to explore FastAPI and related modern Python web technologies to understand API development, authentication systems, and database operations in a practical way.

## Technologies Used

- **Web Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with python-jose
- **Security**: bcrypt password hashing
- **Server**: Uvicorn with automatic reload

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Set up your PostgreSQL database
3. Run: `uvicorn main:app --reload`
4. Visit `/docs` for interactive API documentation
