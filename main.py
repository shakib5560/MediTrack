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


@app.get("/view/{name}")
def view_patient(name: str):
    data = read_json('patients.json')
    if isinstance(data, dict) and "message" in data:
        return data

    name = name.lower()
    matched_patients = []

    for patient in data:
        full_name = patient['name'].lower()
        name_parts = full_name.split()

        # 1. Exact full name match
        if full_name == name:
            return patient

        # 2. First name or last name match
        if name_parts:
            if name_parts[0] == name or name_parts[-1] == name:
                matched_patients.append(patient)

    if matched_patients:
        return matched_patients

    return {"message": "Patient not found"}

