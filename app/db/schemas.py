from typing import Optional
from pydantic import BaseModel
from datetime import datetime


# Role model
class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True


# User model
class UserBase(BaseModel):
    username: str
    email: str
    firstName: str
    lastName: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    # hide it from the response model
    # role_id: int = None
    role: Role = None

    class Config:
        orm_mode = True


class StepBase(BaseModel):
    step_id: str
    substep_id: str
    status: str
    updated_at: datetime
    user_id: Optional[int]


class Step(StepBase):
    id: int
    user: Optional[User]

    class Config:
        orm_mode = True


class StepCreate(StepBase):
    pass


class StepUpdate(StepBase):
    status: str

