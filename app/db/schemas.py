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
    role: Role = None

    class Config:
        orm_mode = True


class StepBase(BaseModel):
    step_id: str
    substep_id: str
    status: str
    doc_uri: Optional[str]
    status_updated_at: Optional[datetime]
    doc_updated_at: Optional[datetime]


class Step(StepBase):
    id: int
    status_user: Optional[User]
    doc_user: Optional[User]

    class Config:
        orm_mode = True


class StepCreate(StepBase):
    pass


class StepUpdate(StepBase):
    status: Optional[str]
    doc_uri: Optional[str]

