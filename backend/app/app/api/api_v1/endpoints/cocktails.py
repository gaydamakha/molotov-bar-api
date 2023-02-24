from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps
from app.schemas.cocktail import cocktail_example

router = APIRouter()


@router.get("/", response_model=schemas.ListOfCocktails, responses={
    200: {
        "content": {
            "application/json": {
                "example": {
                    "cocktails": [cocktail_example.dict()]
                },
            }
        },
        "description": "Return the JSON item or an image.",
    }
}, )
def read_cocktails(
        db: Session = Depends(deps.get_db),
        offset: int = Query(default=0, ge=0),
        limit: int = Query(default=100, ge=0),
        keyword: str | None = Query(default=None, min_length=1, max_length=20),
        ing: str | None = Query(default=None, min_length=1, max_length=20),
) -> Any:
    """
    Retrieve cocktails.
    """
    return {
        'cocktails': crud.cocktail.get_multi(db, offset=offset, limit=limit, keyword=keyword, ing=ing)
    }


# @router.post("/", response_model=schemas.Cocktail)
# def create_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     item_in: schemas.CocktailCreate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Create new item.
#     """
#     item = crud.cocktail.create_with_owner(db=db, obj_in=item_in, owner_id=current_user.id)
#     return item


# @router.put("/{id}", response_model=schemas.Cocktail)
# def update_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     item_in: schemas.CocktailUpdate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Update an item.
#     """
#     item = crud.cocktail.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.cocktail.update(db=db, db_obj=item, obj_in=item_in)
#     return item
#

@router.get("/{id}", response_model=schemas.Cocktail)
def read_cocktail(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
) -> Any:
    """
    Get item by ID.
    """
    item = crud.cocktail.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{id}", response_model=schemas.Cocktail)
def delete_item(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item = crud.cocktail.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.cocktail.remove(db=db, id=id)
    return item
