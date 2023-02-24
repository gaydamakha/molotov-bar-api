from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Ingredient
from app.models.cocktail import Cocktail
from app.schemas.cocktail import CocktailCreate, CocktailUpdate


class CRUDCocktail(CRUDBase[Cocktail, CocktailCreate, CocktailUpdate]):
    def create(self, db: Session, *, obj_in: CocktailCreate) -> Cocktail:
        db_obj = Cocktail(
            name=obj_in.name,
            image_url=obj_in.image_url,
            description=obj_in.description,
            recipe=obj_in.recipe,
            alcohol_degree=obj_in.alcohol_degree,
            category=obj_in.category,
            ingredients=[Ingredient(
                name=i.name,
                measurement=i.measurement,
                quantity=i.quantity,
            ) for i in obj_in.ingredients]
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
            self, db: Session, *, offset: int = 0, limit: int = 100, keyword: str | None = None, ing: str | None = None,
    ) -> List[Cocktail]:
        query = select(Cocktail).offset(offset).limit(limit)
        if keyword is not None:
            query = query.where(Cocktail.name.ilike(f"%{keyword}%"))
        if ing is not None:
            query = query.where(
                Cocktail.ingredients.any(Ingredient.name == ing)
            )
        return db.execute(query).scalars().all()


cocktail = CRUDCocktail(Cocktail)
