"""empty message

Revision ID: 9b3f947c4b10
Revises: 2b67b41fe5e6
Create Date: 2024-10-11 21:58:40.795207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b3f947c4b10'
down_revision: Union[str, None] = '2b67b41fe5e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('matches', 'serialize_tennis')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matches', sa.Column('serialize_tennis', sa.BLOB(), nullable=True))
    # ### end Alembic commands ###
