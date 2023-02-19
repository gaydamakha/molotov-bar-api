import random

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.cocktail import CocktailCreate
from app.tests.utils.utils import random_lower_string
from app.tests.utils.ingredients import create_random_ingredient_create


def create_random_cocktail(db: Session) -> models.Cocktail:
    name = random_lower_string()
    image_url = random_lower_string()
    description = random_lower_string()
    recipe = random_lower_string()
    alcohol_degree = random.uniform(0, 95)
    category = random_lower_string()
    ingredients = [
        create_random_ingredient_create(),
        create_random_ingredient_create(),
    ]
    cocktail_in = CocktailCreate(
        name=name,
        image_url=image_url,
        description=description,
        recipe=recipe,
        alcohol_degree=alcohol_degree,
        category=category,
        ingredients=ingredients
    )
    return crud.cocktail.create(db=db, obj_in=cocktail_in)
