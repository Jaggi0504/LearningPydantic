from pydantic import BaseModel, computed_field
from typing import Dict, List

class Patient(BaseModel):
    name: str
    age: int
    height: float
    weight: float

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    

def insert_patient_data(patient1: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.height)
    print(patient1.weight)
    print(patient1.bmi)
    print("\nValues Inserted")

patient_info = {'name': 'Jagdeep', 'age': 30, 'height': 1.72, 'weight': 55.5}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)