from pydantic import BaseModel, model_validator
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    email: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def valid_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact number")
        
        return model
    
def insert_patient_data(patient1: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.email)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.contact_details)
    print("\nValues Inserted")


patient_info = {'name': 'Jagdeep', 'email': 'abc@abc.com', 'age': 62, 'weight': 55.5, 'married': True,'contact_details': {'phone': '1234567890', 'emergency': '0987654321'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
