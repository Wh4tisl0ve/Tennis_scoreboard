"""empty message

Revision ID: fd8eee33b2ba
Revises: 5d4a0bbb9ec7
Create Date: 2024-10-05 14:05:38.864135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'fd8eee33b2ba'
down_revision: Union[str, None] = '5d4a0bbb9ec7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Matches',
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('player1_id', sa.Integer(), nullable=False),
    sa.Column('player2_id', sa.Integer(), nullable=False),
    sa.Column('winner_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['player1_id'], ['players.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['player2_id'], ['players.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['winner_id'], ['players.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('matches')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matches',
    sa.Column('uuid', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('player1_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('player2_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('winner_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('score', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['player1_id'], ['players.id'], name='matches_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['player2_id'], ['players.id'], name='matches_ibfk_2', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['winner_id'], ['players.id'], name='matches_ibfk_3', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('Matches')
    # ### end Alembic commands ###