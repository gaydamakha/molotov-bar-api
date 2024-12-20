from typing import Generator

import typer
import requests
from urllib.parse import urljoin

from app import crud
from app.db.session import SessionLocal
from app.schemas import CocktailCreate, Ingredient

base_url = 'https://www.thecocktaildb.com/api/json/v1/1/'


def main():
    import_cocktails()


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
            if drink_id in stored_ids:
                continue
            stored_ids.append(drink_id)
            cocktail = get_by_id(drink_id)
            if cocktail is None:
                continue
            ck = crud.cocktail.create(db=db, obj_in=cocktail)
            print(f"created {drink_id} ({ck.id})")


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
        key_index = key.replace('strIngredient', '')
        ingredients.append(Ingredient(
            name=json[key],
            measurement=str(json[f'strMeasure{key_index}']).strip(),
            quantity=0,  # TODO: parse it somehow?
        ))

    return CocktailCreate(
        name=json['strDrink'],
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


if __name__ == "__main__":
    typer.run(main)
