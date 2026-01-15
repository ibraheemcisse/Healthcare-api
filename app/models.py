"""
Patient data models and validation.

This module handles patient data creation with validation.
"""

import uuid
from datetime import datetime


def create_patient_dict(name, age, condition):
    """
    Create a validated patient dictionary.
    
    Args:
        name (str): Patient's full name
        age (int): Patient's age (must be 0-150)
        condition (str): Medical condition/reason for visit
    
    Returns:
        dict: Patient dictionary with id, name, age, condition, registered_at
    
    Raises:
        ValueError: If validation fails
    
    Example:
        >>> patient = create_patient_dict("John Doe", 30, "checkup")
        >>> print(patient['name'])
        John Doe
    """
    if not name:
        raise ValueError("Name cannot be empty")
    if not condition:
        raise ValueError("Condition cannot be empty")
    if not isinstance(age, int) or age < 0 or age > 150:
        raise ValueError("Age must be positive integer between 0-150")
    
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "age": age,
        "condition": condition,
        "registered_at": datetime.now().isoformat()
    }
