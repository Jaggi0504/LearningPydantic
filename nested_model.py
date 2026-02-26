from pydantic import BaseModel

class Address(BaseModel):
    city: str
    province: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Toronto', 'province': 'ON', 'pin': 'ABC2CBA'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Jagdeep', 'gender': 'Male', 'age': 45, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1.address.city)