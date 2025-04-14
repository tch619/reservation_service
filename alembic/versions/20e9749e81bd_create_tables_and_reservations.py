"""Create tables and reservations

Revision ID: 20e9749e81bd
Revises: 
Create Date: 2025-04-14 18:16:19.395583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20e9749e81bd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tables',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('seats', sa.Integer(), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'reservations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('customer_name', sa.String(), nullable=True),
        sa.Column('table_id', sa.Integer(), sa.ForeignKey('tables.id')),
        sa.Column('reservation_time', sa.DateTime(), nullable=True),
        sa.Column('duration_minutes', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('reservations')
    op.drop_table('tables')
