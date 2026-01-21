# Library Management System API (LMS)

A backend-first Library Management System API built with FastAPI and SQLAlchemy, designed with real-world backend practices in mind: layered architecture, authentication, role-based access control, and clean separation of concerns.

This project intentionally focuses on backend correctness and design, not UI.

## 🚀 Features

### Core Functionality

- User management (create, list, retrieve)

- Book management (create, update, list)

- Loan management (issue, return, list loans)

- SQLite-backed relational database using SQLAlchemy ORM

### Authentication & Authorization

- JWT-based authentication

- OAuth2 password flow

- Role-Based Access Control (RBAC)

  - Roles: `ADMIN`, `LIBRARIAN`, `MEMBER`

  - Access to endpoints restricted by role

- Secure password hashing

### Architecture Highlights

- Clean layered structure:

  - API (routers)
  - Services (business logic)
  - Repositories (database access)
  - Schemas (request/response validation)
  - Models (SQLAlchemy ORM)

- Dependency Injection using FastAPI Depends

- UUID-based primary keys

- Environment-based configuration using .env

## 🧱 Tech Stack

- Python 3.12

- FastAPI

- SQLAlchemy 2.x

- SQLite (development database)

- Pydantic

- JWT (python-jose)

- OAuth2

- Uvicorn

### 🔐 Roles & Permissions (RBAC)

- ADMIN

  - Create users

  - Full access to system

- LIBRARIAN

  - Manage books

  - Issue and return loans

- MEMBER

  - View own profile

  - View available books

  - View own loans

Authorization is enforced using FastAPI dependencies, not inside route logic.

### 🗃 Database Design

- Relational schema with proper foreign keys

- UUIDs used as primary identifiers

- Loan records track:

  - Issue date

  - Due date

  - Return date

- Business state (e.g. overdue loans) is derived, not stored

### ⚙️ Environment Configuration

The application uses environment variables for configuration.

Example `.env` file:

```js
DATABASE_URL=sqlite:///./lms.db
SECRET_KEY=DEVELOPMENT
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

INITIAL_ADMIN_EMAIL=admin@example.com
INITIAL_ADMIN_PASSWORD=strongpassword
```

An initial admin account is auto-created if the database is empty.

### ▶️ Running the Project

**1.** Create a virtual environment

**2.** Install dependencies

**3.** Run the server:

```bash
fastapi run
```

Swagger UI available at:

```bash
http://localhost:8000/docs
```

### 🧠 Design Decisions

- FastAPI over Flask for type safety, validation, and dependency injection

- Service + Repository pattern to avoid fat routes

- No hardcoded business states (e.g. overdue loans are computed)

- SQLite first, PostgreSQL planned next

- Focus on correctness over shortcuts

### 🚧 Future Improvements

- PostgreSQL migration

- Alembic migrations

- Background jobs for policy enforcement

- Account suspension automation

- Penalty system for overdue loans

- Deployment (Docker + cloud)

### 📌 Project Status

**Core backend complete.**
This project is considered feature-frozen for now and will be used as a base for:

- Deployment

- Database migration to PostgreSQL

- Production hardening

### 👤 Author

Srijan Kargupta (c) 2026
