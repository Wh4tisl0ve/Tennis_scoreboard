"""empty message

Revision ID: 634f6265750a
Revises: 130ac6328261
Create Date: 2024-10-09 14:22:46.648412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '634f6265750a'
down_revision: Union[str, None] = '130ac6328261'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matches', sa.Column('is_end_game', sa.Boolean(), nullable=False))
    op.alter_column('matches', 'winner_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('matches', 'winner_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('matches', 'is_end_game')
    # ### end Alembic commands ###
