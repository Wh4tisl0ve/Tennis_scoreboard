from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '277366bc9140'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('players',
                    sa.Column('name', sa.String(length=30), nullable=False),
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_players_name'), 'players', ['name'], unique=True)
    op.create_table('matches',
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


def downgrade() -> None:
    op.drop_table('matches')
    op.drop_index(op.f('ix_players_name'), table_name='players')
    op.drop_table('players')
