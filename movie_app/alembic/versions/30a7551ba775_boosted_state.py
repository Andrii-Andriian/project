"""Boosted_State

Revision ID: 30a7551ba775
Revises: 248e98e9ef43
Create Date: 2020-12-21 16:40:35.051458

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '30a7551ba775'
down_revision = '248e98e9ef43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('movie_schedule_id', sa.Integer(), nullable=False))
    op.drop_constraint('reservation_ibfk_1', 'reservation', type_='foreignkey')
    op.create_foreign_key(None, 'reservation', 'movie_schedule', ['movie_schedule_id'], ['id'])
    op.drop_column('reservation', 'date')
    op.drop_column('reservation', 'time')
    op.drop_column('reservation', 'movie_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('movie_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('reservation', sa.Column('time', mysql.VARCHAR(length=20), nullable=False))
    op.add_column('reservation', sa.Column('date', mysql.VARCHAR(length=20), nullable=False))
    op.drop_constraint(None, 'reservation', type_='foreignkey')
    op.create_foreign_key('reservation_ibfk_1', 'reservation', 'movie', ['movie_id'], ['id'])
    op.drop_column('reservation', 'movie_schedule_id')
    # ### end Alembic commands ###