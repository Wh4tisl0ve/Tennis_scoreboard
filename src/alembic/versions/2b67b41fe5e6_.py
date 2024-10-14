"""empty message

Revision ID: 2b67b41fe5e6
Revises: 2b790c09339c
Create Date: 2024-10-11 21:31:21.406249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b67b41fe5e6'
down_revision: Union[str, None] = '2b790c09339c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matches', sa.Column('serialize_tennis', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('matches', 'serialize_tennis')
    # ### end Alembic commands ###
