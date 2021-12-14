"""add foreign-key to posts table

Revision ID: f581d6513f43
Revises: b532c22e777c
Create Date: 2021-12-14 10:32:29.305139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f581d6513f43'
down_revision = 'b532c22e777c'
branch_labels = None
depends_on = None


def upgrade():
	op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
	op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
	op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
	nullable=False, server_default=sa.text('NOW()')))
	op.create_foreign_key('post_users_fk', source_table="posts", referent_table='users',
	local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')

def downgrade():
	op.drop_constraint('post_users_fk', table_name="posts")
	op.drop_column('posts', 'owner_id')
	op.drop_column('posts', 'published')
	op.drop_column('posts', 'created_at')
