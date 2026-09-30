"""merge migration heads

Revision ID: 358cc777afb0
Revises: 70410c5598ec, 0844d29b17b6
Create Date: 2026-09-30 09:46:20.354083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '358cc777afb0'
down_revision: Union[str, Sequence[str], None] = ('70410c5598ec', '0844d29b17b6')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
