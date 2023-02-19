from typing import Optional

from pydantic import BaseModel

from app.schemas.ingredient import Ingredient, ingredient_example


# Shared properties
class CocktailBase(BaseModel):
    name: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None
    recipe: Optional[str] = None
    alcohol_degree: Optional[float] = None
    category: Optional[str] = None
    ingredients: Optional[list[Ingredient]] = None


# Properties to receive on item creation
class CocktailCreate(CocktailBase):
    name: str
    image_url: str
    description: str
    recipe: str
    category: str
    ingredients: list[Ingredient]


# Properties to receive on item update
class CocktailUpdate(CocktailBase):
    pass


# Properties shared by models stored in DB
class CocktailInDBBase(CocktailBase):
    id: int
    name: str
    image_url: str
    description: str
    recipe: str
    alcohol_degree: Optional[float] = None
    category: str
    ingredients: list[Ingredient]

    class Config:
        orm_mode = True


# Properties to return to client
class Cocktail(CocktailInDBBase):
    pass


class ListOfCocktails(BaseModel):
    cocktails: list[Cocktail] = []


# Properties stored in DB
class CocktailInDB(CocktailInDBBase):
    pass


cocktail_example = Cocktail(
    id=1,
    name="Mojito",
    image_url="some/url",
    description="something",
    recipe="something else",
    alcohol_degree=12.0,
    category="Shots",
    ingredients=[ingredient_example],
)
