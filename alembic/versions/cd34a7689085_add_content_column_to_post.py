"""Add content column to Post

Revision ID: cd34a7689085
Revises: 6112918423de
Create Date: 2023-03-09 15:24:21.114468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd34a7689085'
down_revision = '6112918423de'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
