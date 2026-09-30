""" tables changed

Revision ID: 0844d29b17b6
Revises: ae6e2f1fb638
Create Date: 2026-09-29 17:40:13.441587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0844d29b17b6'
down_revision: Union[str, Sequence[str], None] = 'ae6e2f1fb638'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
