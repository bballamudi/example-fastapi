"""add user table

Revision ID: b532c22e777c
Revises: 247c8bf61594
Create Date: 2021-12-14 10:19:50.241402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b532c22e777c'
down_revision = '247c8bf61594'
branch_labels = None
depends_on = None


def upgrade():
	op.create_table('users',
									sa.Column('id', sa.Integer(), nullable=False),
									sa.Column('email', sa.String(), nullable=False),
									sa.Column('password', sa.String(), nullable=False),
									sa.Column('created_at', sa.TIMESTAMP(timezone=True),
									server_default=sa.text('now()'), nullable=False),
									sa.PrimaryKeyConstraint('id'),
									sa.UniqueConstraint('email')
	)


def downgrade():
  op.drop_table('users')
