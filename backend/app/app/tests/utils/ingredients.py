import random

from app.schemas.ingredient import IngredientCreate
from app.tests.utils.utils import random_lower_string


def create_random_ingredient_create() -> IngredientCreate:
    name = random_lower_string()
    title = random_lower_string()
    measurement = random_lower_string()
    quantity = random.uniform(0, 5)
    return IngredientCreate(
        name=name,
        title=title,
        measurement=measurement,
        quantity=quantity,
    )
