"""empty message

Revision ID: b1b2be4d7c56
Revises: 9a8ab8d09a49
Create Date: 2024-10-12 19:00:59.171509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b1b2be4d7c56'
down_revision: Union[str, None] = '9a8ab8d09a49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matchstory',
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('score', sa.JSON(), nullable=False),
    sa.Column('match_status', sa.JSON(), nullable=False),
    sa.Column('player_goal', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['uuid'], ['matches.uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('matches', 'score')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matches', sa.Column('score', mysql.JSON(), nullable=True))
    op.drop_table('matchstory')
    # ### end Alembic commands ###
