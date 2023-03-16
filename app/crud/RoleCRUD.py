from app.db.schemas import RoleCreate, RoleUpdate
from app.crud.base import CRUDBase
from app.models import Role


class RoleCRUD(CRUDBase[Role, RoleCreate, RoleUpdate]):
    ...


roleCRUD = RoleCRUD(Role)
