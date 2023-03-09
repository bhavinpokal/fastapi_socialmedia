"""Add fk to Post

Revision ID: 30224f82dd3c
Revises: a7e1f16ced22
Create Date: 2023-03-09 15:34:35.984622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30224f82dd3c'
down_revision = 'a7e1f16ced22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
