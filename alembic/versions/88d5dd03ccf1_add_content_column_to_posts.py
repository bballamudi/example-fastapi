"""add content column to posts

Revision ID: 88d5dd03ccf1
Revises: f581d6513f43
Create Date: 2021-12-14 10:44:38.980653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88d5dd03ccf1'
down_revision = 'f581d6513f43'
branch_labels = None
depends_on = None


def upgrade():
	op.add_column('posts', sa.Column('content', sa.String, nullable=False))


def downgrade():
	op.drop_column('posts', 'content')
