from fastapi import FastAPI
import xml.etree.ElementTree as ET

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Application Python démarrée"}

@app.get("/employees")
def get_employees():
    tree = ET.parse("employ.xml")
    root = tree.getroot()

    employees = []
    for emp in root.findall("employee"):
        employees.append({
            "id": emp.find("id").text,
            "name": emp.find("name").text,
            "role": emp.find("role").text
        })

    return employees
