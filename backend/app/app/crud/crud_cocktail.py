from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Ingredient
from app.models.cocktail import Cocktail
from app.schemas.cocktail import CocktailCreate, CocktailUpdate


class CRUDCocktail(CRUDBase[Cocktail, CocktailCreate, CocktailUpdate]):
    def create(self, db: Session, *, obj_in: CocktailCreate) -> Cocktail:
        db_obj = Cocktail(
            name=obj_in.name,
            title=obj_in.title,
            image_url=obj_in.image_url,
            description=obj_in.description,
            recipe=obj_in.recipe,
            alcohol_degree=obj_in.alcohol_degree,
            ingredients=[Ingredient(
                name=i.name, title=i.title, measurement=i.measurement, quantity=i.quantity,
            ) for i in obj_in.ingredients]
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


cocktail = CRUDCocktail(Cocktail)
