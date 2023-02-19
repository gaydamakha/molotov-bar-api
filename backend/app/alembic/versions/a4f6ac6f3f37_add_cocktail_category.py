"""add cocktail category

Revision ID: a4f6ac6f3f37
Revises: bfb864d59be2
Create Date: 2023-02-09 12:16:51.163219

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a4f6ac6f3f37'
down_revision = 'bfb864d59be2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "cocktail",
        sa.Column("category", sa.String(), nullable=False),
    )


def downgrade():
    op.drop_column('cocktail', 'category')
