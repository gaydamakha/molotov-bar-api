from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Ingredient


class CRUDIngredient(CRUDBase[str, None, None]):
    def get_multi(
        self, db: Session, *, offset: int = 0, limit: int = 100
    ) -> List[str]:
        return db.execute(select(Ingredient.name).distinct().offset(offset).limit(limit)).scalars().all()


ingredient = CRUDIngredient(Ingredient)
