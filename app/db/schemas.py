from typing import Optional
from pydantic import BaseModel


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


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    roles: list[Role] = []

    class Config:
        orm_mode = True


class StepBase(BaseModel):
    step_id: str
    substep_id: str
    status: str


class Step(StepBase):
    id: int

    class Config:
        orm_mode = True


class StepCreate(StepBase):
    pass


class StepUpdate(StepBase):
    status: str

