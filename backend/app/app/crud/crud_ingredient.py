from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Ingredient


class CRUDIngredient(CRUDBase[str, None, None]):
    def get_multi(
        self, db: Session, *, offset: int = 0, limit: int = 100, keyword: str | None = None,
    ) -> List[str]:
        query = select(Ingredient.name).distinct().offset(offset).limit(limit)
        if keyword is not None:
            query = query.where(Ingredient.name.ilike(f"%{keyword}%"))
        return db.execute(query).scalars().all()


ingredient = CRUDIngredient(Ingredient)
