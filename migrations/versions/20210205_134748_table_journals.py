"""table_journals

Revision ID: 150b31345d38
Revises: 473be5d62e68
Create Date: 2021-02-05 13:47:48.604547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '150b31345d38'
down_revision = '473be5d62e68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journals')
    # ### end Alembic commands ###
