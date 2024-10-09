"""empty message

Revision ID: 130ac6328261
Revises: 186e80de1ff2
Create Date: 2024-10-08 13:31:20.618290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '130ac6328261'
down_revision: Union[str, None] = '186e80de1ff2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('players', 'name',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=20),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('players', 'name',
               existing_type=sa.String(length=20),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=False)
    # ### end Alembic commands ###
