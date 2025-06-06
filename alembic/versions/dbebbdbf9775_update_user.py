"""update user

Revision ID: dbebbdbf9775
Revises: bd0ab8d3165b
Create Date: 2025-05-16 19:31:09.225463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'dbebbdbf9775'
down_revision: Union[str, None] = 'bd0ab8d3165b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'data',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'data',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               nullable=False)
    # ### end Alembic commands ###
