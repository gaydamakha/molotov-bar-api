import random

from sqlalchemy.orm import Session

from app import crud
from app.schemas.cocktail import CocktailCreate
from app.tests.utils.utils import random_lower_string
from app.tests.utils.ingredients import create_random_ingredient_create


def test_create_item(db: Session) -> None:
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
        ingredients=ingredients,
    )
    cocktail = crud.cocktail.create(db=db, obj_in=cocktail_in)
    assert cocktail.name == name
    assert cocktail.category == category
    assert cocktail.image_url == image_url
    assert cocktail.description == description
    assert cocktail.recipe == recipe
    assert cocktail.alcohol_degree == alcohol_degree
    assert len(cocktail.ingredients) == len(ingredients)
    for k, i in enumerate(cocktail.ingredients):
        assert i.id is not None
        assert i.name == ingredients[k].name
        assert i.measurement == ingredients[k].measurement
        assert i.quantity == ingredients[k].quantity
        assert i.cocktail_id == cocktail.id


def test_get_item(db: Session) -> None:
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
    cocktail = crud.cocktail.create(db=db, obj_in=cocktail_in)
    stored_cocktail = crud.cocktail.get(db=db, id=cocktail.id)
    assert stored_cocktail
    assert cocktail.id == stored_cocktail.id
    assert cocktail.name == stored_cocktail.name
    assert cocktail.image_url == stored_cocktail.image_url
    assert cocktail.description == stored_cocktail.description
    assert cocktail.recipe == stored_cocktail.recipe
    assert cocktail.alcohol_degree == stored_cocktail.alcohol_degree
    assert cocktail.category == stored_cocktail.category
    assert len(cocktail.ingredients) == len(ingredients)
    for k, i in enumerate(cocktail.ingredients):
        assert i.id is not None
        assert i.name == ingredients[k].name
        assert i.measurement == ingredients[k].measurement
        assert i.quantity == ingredients[k].quantity
        assert i.cocktail_id == cocktail.id


# def test_update_item(db: Session) -> None:
#     title = random_lower_string()
#     description = random_lower_string()
#     item_in = CocktailCreate(title=title, description=description)
#     user = create_random_user(db)
#     item = crud.cocktail.create_with_owner(db=db, obj_in=item_in, owner_id=user.id)
#     description2 = random_lower_string()
#     item_update = CocktailUpdate(description=description2)
#     item2 = crud.cocktail.update(db=db, db_obj=item, obj_in=item_update)
#     assert item.id == item2.id
#     assert item.title == item2.title
#     assert item2.description == description2
#     assert item.owner_id == item2.owner_id
#
#
def test_delete_item(db: Session) -> None:
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
        ingredients=ingredients,
    )
    item = crud.cocktail.create(db=db, obj_in=cocktail_in)
    item2 = crud.cocktail.remove(db=db, id=item.id)
    item3 = crud.cocktail.get(db=db, id=item.id)
    assert item3 is None
    assert item2.id == item.id
