# Healthcare Appointment System

REST API for managing patient appointments and doctor schedules.

## Overview

A FastAPI-based healthcare management system demonstrating modern API design, data validation, and database operations. Built with PostgreSQL backend and containerized for deployment.

## Tech Stack

- **Backend:** Python 3.12, FastAPI
- **Database:** PostgreSQL (planned)
- **Storage:** JSON (current), migrating to PostgreSQL
- **Containerization:** Docker (planned)

## Features

**Patient Management**
- Patient registration with validation
- Search and filter capabilities
- Appointment scheduling
- UUID-based identification

**Data Operations**
- Input validation (Pydantic models)
- JSON persistence with error handling
- Modular architecture
- RESTful API design (in progress)

## Project Structure
```
healthcare-api/
├── app/
│   ├── models.py       # Data models and validation
│   ├── registry.py     # Core business logic
│   └── utils.py        # Utility functions
└── test_modules.py     # Integration tests
```

## Quick Start
```bash
git clone https://github.com/ibraheemcisse/healthcare-api.git
cd healthcare-api

# Test current implementation
python3 test_modules.py
```

## API Endpoints (Coming Soon)
```
POST   /patients              Create patient record
GET    /patients              List all patients
GET    /patients/{id}         Get patient by ID
POST   /appointments          Schedule appointment
GET    /doctors/{id}/schedule View doctor appointments
```

## Current Status

**Completed:**
- Core patient management logic
- Data validation layer
- File-based persistence
- Modular code organization

**In Progress:**
- FastAPI REST endpoints
- PostgreSQL migration
- Docker containerization
- Deployment configuration

## Development Roadmap

- **Week 2:** REST API with FastAPI
- **Week 3:** PostgreSQL integration with migrations
- **Week 4:** Docker containerization and deployment
- **Week 5+:** Kubernetes deployment (separate lab project)

## Skills Demonstrated

- Python application architecture
- Data validation and error handling
- Modular design patterns
- API design principles
- Version control practices

## License

MIT

## Contact

Ibrahim Cisse - [LinkedIn](https://linkedin.com/in/ibraheemcisse) - [Medium](https://medium.com/@Ibraheemcisse)

Project Link: https://github.com/ibraheemcisse/healthcare-api
