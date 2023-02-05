from typing import Optional

from pydantic import BaseModel


# Shared properties
class CocktailBase(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None
    recipe: Optional[str] = None
    alcohol_degree: Optional[float] = None


# Properties to receive on item creation
class CocktailCreate(CocktailBase):
    name: str
    title: str
    image_url: str
    description: str
    recipe: str


# Properties to receive on item update
class CocktailUpdate(CocktailBase):
    pass


# Properties shared by models stored in DB
class CocktailInDBBase(CocktailBase):
    id: int
    name: str
    title: str
    image_url: str
    description: str
    recipe: str
    alcohol_degree: Optional[float] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Cocktail(CocktailInDBBase):
    pass


# Properties stored in DB
class CocktailInDB(CocktailInDBBase):
    pass
