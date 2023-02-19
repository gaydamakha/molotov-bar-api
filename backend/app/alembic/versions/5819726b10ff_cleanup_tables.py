"""cleanup tables

Revision ID: 5819726b10ff
Revises: a4f6ac6f3f37
Create Date: 2023-02-12 16:08:41.171035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5819726b10ff'
down_revision = 'a4f6ac6f3f37'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        table_name="cocktail",
        column_name="name",
        new_column_name="tmp"
    )
    op.alter_column(
        table_name="cocktail",
        column_name="title",
        new_column_name="name",
    )
    op.drop_column(
        table_name="cocktail",
        column_name="tmp"
    )
    op.alter_column(
        table_name="ingredient",
        column_name="name",
        new_column_name="tmp"
    )
    op.alter_column(
        table_name="ingredient",
        column_name="title",
        new_column_name="name",
    )
    op.drop_column(
        table_name="ingredient",
        column_name="tmp"
    )


def downgrade():
    op.alter_column(
        table_name="cocktail",
        column_name="name",
        new_column_name="title",
    )
    op.add_column(
        table_name="cocktail",
        column=sa.Column("name", sa.String(), nullable=False, server_default=str("")),
    )
    op.alter_column(
        table_name="ingredient",
        column_name="name",
        new_column_name="title",
    )
    op.add_column(
        table_name="ingredient",
        column=sa.Column("name", sa.String(), nullable=False, server_default=str("")),
    )
