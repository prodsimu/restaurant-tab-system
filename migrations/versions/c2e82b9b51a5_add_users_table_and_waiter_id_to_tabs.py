"""add users table and waiter_id to tabs

Revision ID: c2e82b9b51a5
Revises: 53849b8a8501
Create Date: 2026-06-26 13:22:14.667383

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2e82b9b51a5'
down_revision: Union[str, Sequence[str], None] = '53849b8a8501'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

role_enum = sa.Enum('admin', 'waiter', name='roleenum')


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('password_hash', sa.String(), nullable=False),
        sa.Column('role', role_enum, nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)

    op.add_column('tabs', sa.Column('waiter_id', sa.Integer(), nullable=True))

    bind = op.get_bind()
    tabs_count = bind.execute(sa.text('SELECT COUNT(*) FROM tabs')).scalar_one()

    if tabs_count:
        legacy_waiter_id = bind.execute(
            sa.text(
                """
                INSERT INTO users (username, password_hash, role)
                VALUES ('legacy_waiter', 'legacy-migration-placeholder', 'waiter')
                RETURNING id
                """
            )
        ).scalar_one()

        bind.execute(
            sa.text(
                'UPDATE tabs SET waiter_id = :waiter_id WHERE waiter_id IS NULL'
            ),
            {'waiter_id': legacy_waiter_id},
        )

    op.alter_column('tabs', 'waiter_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key(
        'fk_tabs_waiter_id_users',
        'tabs',
        'users',
        ['waiter_id'],
        ['id'],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_tabs_waiter_id_users', 'tabs', type_='foreignkey')
    op.drop_column('tabs', 'waiter_id')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    role_enum.drop(op.get_bind(), checkfirst=True)
