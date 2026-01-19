"""
FastAPI application entry point.
"""

from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="Healthcare Appointment API",
    description="API for managing patient appointments",
    version="0.1.0"
)

@app.get("/")
def root():
    """Root endpoint - API info"""
    return {
        "service": "Healthcare Appointment API",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "healthcare-api"
    }
