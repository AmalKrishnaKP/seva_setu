"""user table updated

Revision ID: df295d777f07
Revises: 459834bfb1a4
Create Date: 2026-09-21 01:48:19.567030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'df295d777f07'
down_revision: Union[str, Sequence[str], None] = '459834bfb1a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
