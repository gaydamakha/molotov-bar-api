from app.crud.base import CRUDBase
from app.models.cocktail import Cocktail
from app.schemas.cocktail import CocktailCreate, CocktailUpdate


class CRUDCocktail(CRUDBase[Cocktail, CocktailCreate, CocktailUpdate]):
    pass


cocktail = CRUDCocktail(Cocktail)
