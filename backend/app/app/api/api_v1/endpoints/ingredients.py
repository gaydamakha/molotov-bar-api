from typing import Any

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=schemas.ListOfIngredients, responses={
    200: {
        "content": {
            "application/json": {
                "example": {
                    "ingredients": ["Lemon juice", "Light rum", "Cocoa "]
                },
            }
        },
        "description": "Returns the list of available ingredients",
    }
}, )
def read_ingredients(
        db: Session = Depends(deps.get_db),
        offset: int = Query(default=0, ge=0),
        limit: int = Query(default=100, ge=0),
        keyword: str | None = Query(default=None, max_length=15)
) -> Any:
    """
    Retrieve ingredients.
    """
    return {
        'ingredients': crud.ingredient.get_multi(db, offset=offset, limit=limit, keyword=keyword)
    }
