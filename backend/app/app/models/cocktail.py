from sqlalchemy import Column, Integer, String, Text, Float

from app.db.base_class import Base


class Cocktail(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    title = Column(String, index=True)
    image_url = Column(String)
    description = Column(Text)
    recipe = Column(Text)
    alcohol_degree = Column(Float)
