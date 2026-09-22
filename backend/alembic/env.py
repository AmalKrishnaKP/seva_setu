from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
import sys
import os
sys.path.insert(0, os.path.abspath('src'))

from core.session import base
from domain.user.model import User


from alembic import context

from src.core.session import Base

# Import all models so Alembic can detect them
from src.domain.user.model import User
from src.domain.worker.model import Worker
from src.domain.auth.model import UserSession


# Alembic Config object
config = context.config


# Configure Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# SQLAlchemy metadata
target_metadata = Base.metadata

def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table" and name in {
        'spatial_ref_sys', 'topology', 'layer', 'direction_lookup',
        'secondary_unit_lookup', 'edges', 'pagc_gaz', 'addr', 'zcta5',
        'bg', 'pagc_rules', 'loader_lookuptables', 'state', 'pagc_lex',
        'county_lookup', 'place', 'cousub', 'zip_lookup', 'zip_state_loc',
        'geocode_settings', 'county', 'geocode_settings_default',
        'zip_lookup_base', 'tract', 'faces', 'zip_state', 'street_type_lookup',
        'tabblock20', 'countysub_lookup', 'place_lookup', 'loader_platform',
        'zip_lookup_all', 'state_lookup', 'loader_variables', 'tabblock',
        'featnames', 'addrfeat'
    }:
        return False
    return True

def include_name(name, type_, parent_names):
    """
    Tell Alembic which database objects should be considered
    during autogeneration.
    """

    # Only consider public schema
    if type_ == "schema":
        return name in (None, "public")

    # Only consider tables in public schema
    if type_ == "table":
        schema_name = parent_names.get("schema_name")

        if schema_name not in (None, "public"):
            return False

        # PostGIS-managed table
        if name == "spatial_ref_sys":
            return False

    return True


def run_migrations_offline() -> None:
    """Run migrations in offline mode."""

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
        include_name=include_name,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in online mode."""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        # Only use the application's public schema
        connection.execute(
            text("SET search_path TO public")
        )
        # SQLAlchemy 2 starts an implicit transaction for the SET command.
        # Finish it before Alembic opens and commits its migration transaction.
        connection.commit()

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            include_name=include_name,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
