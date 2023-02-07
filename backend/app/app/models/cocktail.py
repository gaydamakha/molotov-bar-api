from typing import List, TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import Mapped, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .ingredient import Ingredient


class Cocktail(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    title = Column(String, index=True)
    image_url = Column(String)
    description = Column(Text)
    recipe = Column(Text)
    alcohol_degree = Column(Float)
    ingredients: Mapped[List["Ingredient"]] = relationship(cascade="all, delete")
