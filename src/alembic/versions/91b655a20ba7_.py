"""empty message

Revision ID: 91b655a20ba7
Revises: 3a4ad2de8f9f
Create Date: 2024-10-12 20:34:13.570695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '91b655a20ba7'
down_revision: Union[str, None] = '3a4ad2de8f9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('matchstory', 'player_goal',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('matchstory', 'player_goal',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
