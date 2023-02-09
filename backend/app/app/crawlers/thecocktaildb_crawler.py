from typing import Generator

import requests
from urllib.parse import urljoin

from app import crud
from app.db.session import SessionLocal
from app.schemas import CocktailCreate, Ingredient

base_url = 'https://www.thecocktaildb.com/api/json/v1/1/'


def import_cocktails():
    db = SessionLocal()
    ingredients = get_all_ingredients()
    stored_ids = []

    for ing in ingredients:
        url = urljoin(base_url, f'filter.php?i={ing}')
        response = requests.request('GET', url)
        json = response.json()
        for drink in json['drinks']:
            drink_id = drink['idDrink']
            if drink_id not in stored_ids:
                stored_ids.append(drink_id)
                cocktail = get_by_id(drink_id)
                crud.cocktail.create(db=db, obj_in=cocktail)


def get_by_id(drink_id: str) -> CocktailCreate | None:
    url = urljoin(base_url, f'lookup.php?i={drink_id}')
    response = requests.request('GET', url)
    if response.status_code != 200 and response.status_code != 304:
        return None
    drinks = response.json()['drinks']
    if drinks is None:
        return None

    return from_cocktail_db_json(drinks[0])


def from_cocktail_db_json(json: dict) -> CocktailCreate:
    ingredients = []
    json_ingredients_keys = [k for k in json.keys() if k.startswith('strIngredient') and json[k] is not None]
    for key in json_ingredients_keys:
        ingredient_name = json[key]
        key_index = key.replace('strIngredient', '')
        measurement = str(json[f'strMeasure{key_index}']).strip()
        ingredients.append(Ingredient(
            name='',
            title=ingredient_name,
            measurement=measurement,
            quantity=0,  # TODO: parse it somehow?
        ))

    return CocktailCreate(
        name=json['idDrink'],
        title=json['strDrink'],
        image_url=json['strDrinkThumb'],
        description='',
        recipe=str(json['strInstructions']).strip(),
        alcohol_degree=None,
        category=str(json['strCategory']).strip(),
        ingredients=ingredients,
    )


def get_all_ingredients() -> Generator:
    url = urljoin(base_url, 'list.php?i=list')
    response = requests.request('GET', url)
    json = response.json()
    for ingredient in json['drinks']:
        yield ingredient['strIngredient1']


if __name__ == '__main__':
    import_cocktails()
