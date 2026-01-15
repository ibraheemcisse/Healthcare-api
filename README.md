# Healthcare Appointment System

REST API for managing patient appointments - built as part of SRE portfolio demonstrating production-ready development practices.

## Project Status
✅ **Phase 1 Complete** - Python fundamentals, data structures, modular code organization

## Tech Stack

**Current (Phase 1):**
- Python 3.12
- JSON file storage
- Modular architecture

**Planned:**
- **Phase 2:** FastAPI REST API
- **Phase 3:** PostgreSQL database
- **Phase 4:** Redis caching
- **Phase 5:** Docker containerization
- **Phase 6:** eBPF observability

## Project Structure
```
healthcare-api/
├── app/
│   ├── models.py       # Patient data models & validation
│   ├── registry.py     # PatientRegistry class (CRUD operations)
│   └── utils.py        # Utility functions
├── phase1_day*.py      # Learning progression (Phase 1)
└── test_modules.py     # Module testing
```

## Features Implemented

### Phase 1 - Python Fundamentals (Complete)
- [x] UUID generation for unique patient IDs
- [x] ISO timestamp tracking
- [x] Input validation (name, age, condition)
- [x] JSON persistence (save/load)
- [x] CRUD operations
  - Create patients
  - Read (search by name, filter by age, find by ID)
  - Update (schedule appointments)
  - Delete operations
- [x] Error handling (file operations, corrupted data)
- [x] List comprehensions for filtering
- [x] DateTime operations (appointment scheduling)
- [x] Modular code organization

## Installation & Usage
```bash
# Clone repository
git clone https://github.com/ibraheemcisse/healthcare-api.git
cd healthcare-api

# Test Phase 1 modules
python3 test_modules.py
```

## Learning Goals

This project demonstrates:
- Production-quality Python code
- Error handling patterns
- Data validation
- Modular architecture
- Test-driven development
- Version control best practices

## Next Steps

**Phase 2 (Starting Next):** FastAPI REST API
- POST /patients - Register patient
- GET /patients - List patients
- POST /appointments - Book appointment
- GET /doctors/{id}/appointments - Doctor schedules

## Progress Tracking

- **Week 1:** ✅ Python fundamentals complete
- **Week 2:** 🚧 FastAPI REST API (upcoming)
- **Week 3-4:** PostgreSQL integration
- **Week 5:** Redis caching
- **Week 6:** Docker containerization
- **Week 7-8:** eBPF observability + CKA prep

---

*Part of 12-week SRE portfolio project. See commit history for development progression.*
