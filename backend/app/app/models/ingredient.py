from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped

from app.db.base_class import Base


class Ingredient(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # TODO: fill it with a string id
    title = Column(String, index=True)
    measurement = Column(String)
    quantity = Column(Float)
    cocktail_id: Mapped[int] = Column(Integer, ForeignKey("cocktail.id"))
