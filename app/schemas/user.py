from pydantic import BaseModel, constr, EmailStr

class UserCreate(BaseModel):
    first_name: constr(min_length=1, max_length=50)
    last_name: constr(min_length=1, max_length=50)
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=6, max_length=72)  
    phone_number: constr(min_length=10, max_length=15)
    age: int
    gender: constr(min_length=1, max_length=10)

class UserRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    phone_number: str
    age: int
    gender: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True
