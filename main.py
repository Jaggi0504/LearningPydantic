from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str = Field(max_length=50)
    age: int = Field(gt=0, lt=100)
    weight: float = Field(gt=0)
    married: bool = False
    allergies: Optional[List[str]] = None

def insert_patient_data(patient1: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.allergies)
    print(patient1.weight)
    print(patient1.married)
    print("Inserted")


patient_info = {'name': 'Jagdeep', 'age': 30, 'weight': 55.5}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)