"""tables changed

Revision ID: 6698db4f421d
Revises: 98eaea42c5ca
Create Date: 2026-09-29 12:29:40.724483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6698db4f421d'
down_revision: Union[str, Sequence[str], None] = '98eaea42c5ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    language_enum = sa.Enum('MAL', 'ENG', 'TAM', 'TEL', 'HIN', name='languageenum')
    language_enum.create(op.get_bind(), checkfirst=True)
    op.add_column('users', sa.Column('language', language_enum, nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'language')
    language_enum = sa.Enum('MAL', 'ENG', 'TAM', 'TEL', 'HIN', name='languageenum')
    language_enum.drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###
