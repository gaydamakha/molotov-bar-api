from typing import Optional

from pydantic import BaseModel


# Shared properties
class IngredientBase(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    measurement: Optional[str] = None
    quantity: Optional[float] = None


class IngredientCreate(IngredientBase):
    name: str
    title: str


class IngredientUpdate(IngredientBase):
    pass


# Properties shared by models stored in DB
class IngredientInDBBase(IngredientBase):
    name: str
    title: str

    class Config:
        orm_mode = True


# Properties to return to client
class Ingredient(IngredientInDBBase):
    pass


# Properties stored in DB
class IngredientInDB(IngredientInDBBase):
    pass


ingredient_example = Ingredient(
    id=11,
    name="Mint",
    title="someTitle",
    quantity="2",
    measurement="piece"
)

