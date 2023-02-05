from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.cocktail import create_random_cocktail


# def test_create_item(
#     client: TestClient, superuser_token_headers: dict, db: Session
# ) -> None:
#     data = {"title": "Foo", "description": "Fighters"}
#     response = client.post(
#         f"{settings.API_V1_STR}/items/", headers=superuser_token_headers, json=data,
#     )
#     assert response.status_code == 200
#     content = response.json()
#     assert content["title"] == data["title"]
#     assert content["description"] == data["description"]
#     assert "id" in content
#     assert "owner_id" in content


def test_read_cocktail(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    cocktail = create_random_cocktail(db)
    response = client.get(
        f"{settings.API_V1_STR}/cocktails/{cocktail.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == cocktail.id
    assert content["name"] == cocktail.name
    assert content["title"] == cocktail.title
    assert content["image_url"] == cocktail.image_url
    assert content["description"] == cocktail.description
    assert content["recipe"] == cocktail.recipe
    assert content["alcohol_degree"] == cocktail.alcohol_degree
