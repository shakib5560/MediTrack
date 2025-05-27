from fastapi import FastAPI
from logics import read_json

app = FastAPI()

    
@app.get("/")
def home():
    return {"message": "patients management system API using FastAPI"}

@app.get("/about")
def about():
    return {
        "name": "Patients Management System API",
        "version": "1.0.0",
        "description": "An API for managing patient records, appointments, and medical history."
    }
    
@app.get("/viewall")
def view_all():
    data = read_json('patients.json')
    if isinstance(data, dict) and "message" in data:
        return data
    return {"patients": data}    