from pydantic import BaseModel, Field, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int
    email: str
    weight: float
    married: bool = Field(default=False)
    allergies: Optional[List[str]] = None

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['abc.com', 'def.com']
        domain_name=value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before') #mode=before means before coercion pydantic will check and not act smart to convert string to int in age. By default the mode=after, so even if we give string, it will convert into int
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be between 0 and 100')


def insert_patient_data(patient1: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.email)
    print(patient1.weight)
    print(patient1.married)
    print(patient1.allergies)
    print("\nValues Inserted")

patient_info = {'name': 'Jagdeep', 'age': 30, 'email': 'abc@abc.com', 'weight': 55.5}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)