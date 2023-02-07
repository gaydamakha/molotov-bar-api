"""Add cocktail ingredients

Revision ID: bfb864d59be2
Revises: d4867f3a4c0a
Create Date: 2023-02-05 18:45:21.116542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfb864d59be2'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ingredient",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("measurement", sa.String(), nullable=False),
        sa.Column("quantity", sa.Float(), nullable=False),
        sa.Column("cocktail_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["cocktail_id"], ["cocktail.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_ingredient_id"), "ingredient", ["id"], unique=False)
    op.create_index(op.f("ix_ingredient_name"), "ingredient", ["name"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_ingredient_name"), table_name="ingredient")
    op.drop_index(op.f("ix_ingredient_id"), table_name="ingredient")
    op.drop_table("ingredient")
