"""create post table

Revision ID: 247c8bf61594
Revises: 
Create Date: 2021-12-13 19:47:42.243443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '247c8bf61594'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, 
	primary_key=True), sa.Column('title', sa.String(), nullable=False))
	pass

def downgrade():
	op.drop_table('posts')
	pass
