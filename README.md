# Healthcare Appointment System

A healthcare management service demonstrating full-stack system ownership from an infrastructure engineering perspective.

## Overview

This service manages patient records, appointments, and doctor schedules. It's built incrementally with a focus on correctness, reliability, and operational thinking — applying SRE principles to application development.

## Why This Project Exists

Most SREs operate services built by others. This project bridges that gap by owning the entire stack: API design, data models, persistence, deployment, and observability.

**Goal:** Demonstrate how application code, infrastructure, and operations integrate in real systems.

## Current Implementation

**Core Features:**
- Patient registration and management
- Appointment scheduling
- Doctor schedule queries
- UUID-based identifiers
- Input validation and error handling
- Modular architecture

**Tech Stack:**
- Python 3.12
- JSON persistence (migrating to PostgreSQL)
- Modular service design

## Project Structure
```
healthcare-api/
├── app/
│   ├── models.py       # Data models and validation
│   ├── registry.py     # Core business logic
│   └── utils.py        # Utilities
└── test_modules.py     # Integration tests
```

Business logic is isolated from transport layer (API/storage) for testability and reusability.

## Development Phases

**Phase 1 (Complete):** Core logic, validation, file-based storage  
**Phase 2 (In Progress):** FastAPI REST endpoints  
**Phase 3 (Upcoming):** PostgreSQL + migrations  
**Phase 4 (Upcoming):** Docker deployment  
**Phase 5 (Planned):** Observability (Prometheus, health checks, SLOs)

## Running Locally
```bash
git clone https://github.com/ibraheemcisse/healthcare-api.git
cd healthcare-api
python3 test_modules.py
```

## API Design (Coming Soon)
```
POST   /patients              Create patient
GET    /patients              List patients
GET    /patients/{id}         Get patient details
POST   /appointments          Schedule appointment
GET    /doctors/{id}/schedule View appointments
```

## Skills Demonstrated

- Service-oriented architecture
- Data validation and integrity
- API design patterns
- Modular code organization
- Incremental development
- SRE mindset applied to application development

## What's Next

- REST API with FastAPI
- PostgreSQL integration
- Container deployment
- Prometheus metrics
- Health monitoring

---

**Contact:** Ibrahim Cisse | [LinkedIn](https://linkedin.com/in/ibraheemcisse) | [Medium](https://medium.com/@Ibraheemcisse)
