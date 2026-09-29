from logging.config import fileConfig
import os
import sys

from alembic import context
from sqlalchemy import engine_from_config, pool, text

# Make src/ importable
sys.path.insert(0, os.path.abspath("src"))

# SQLAlchemy Base
from src.core.session import Base

<<<<<<< HEAD
# Import ALL models so Alembic can detect their tables
from src.domain.user.model import User
from src.domain.worker.model import Worker
from src.domain.badge.model import Badge, WorkerBadge
from src.domain.favorite.model import Favorite
=======
# Import server which in turn imports all models
# import src.server
# from src.domain.auth.model import UserSession

>>>>>>> otp_system

# ---------------------------------------------------------
# Alembic Config
# ---------------------------------------------------------

config = context.config


# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# ---------------------------------------------------------
# Metadata
# ---------------------------------------------------------

target_metadata = Base.metadata


# ---------------------------------------------------------
# Ignore PostGIS/system tables
# ---------------------------------------------------------

POSTGIS_TABLES = {
    "spatial_ref_sys",
    "topology",
    "layer",
    "direction_lookup",
    "secondary_unit_lookup",
    "edges",
    "pagc_gaz",
    "addr",
    "zcta5",
    "bg",
    "pagc_rules",
    "loader_lookuptables",
    "state",
    "pagc_lex",
    "county_lookup",
    "place",
    "cousub",
    "zip_lookup",
    "zip_state_loc",
    "geocode_settings",
    "county",
    "geocode_settings_default",
    "zip_lookup_base",
    "tract",
    "faces",
    "zip_state",
    "street_type_lookup",
    "tabblock20",
    "countysub_lookup",
    "place_lookup",
    "loader_platform",
    "zip_lookup_all",
    "state_lookup",
    "loader_variables",
    "tabblock",
    "featnames",
    "addrfeat",
}


def include_object(
    object,
    name,
    type_,
    reflected,
    compare_to,
):
    """
    Prevent Alembic from managing PostGIS/system tables.
    """

    if type_ == "table" and name in POSTGIS_TABLES:
        return False

    return True


def include_name(name, type_, parent_names):
    """
    Tell Alembic which schemas/tables should be considered.
    """

    # Only public schema
    if type_ == "schema":
        return name in (None, "public")

    # Only public-schema tables
    if type_ == "table":
        schema_name = parent_names.get("schema_name")

        if schema_name not in (None, "public"):
            return False

        # Ignore PostGIS table
        if name == "spatial_ref_sys":
            return False

    return True


# ---------------------------------------------------------
# Offline migrations
# ---------------------------------------------------------

def run_migrations_offline() -> None:
    """
    Run migrations without connecting to the database.
    """

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named"
        },
        include_schemas=True,
        include_name=include_name,
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


# ---------------------------------------------------------
# Online migrations
# ---------------------------------------------------------

def run_migrations_online() -> None:
    """
    Run migrations with a database connection.
    """

    connectable = engine_from_config(
        config.get_section(
            config.config_ini_section,
            {}
        ),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        # Use PostgreSQL public schema
        connection.execute(
            text("SET search_path TO public")
        )

        # Finish the transaction created by SET
        connection.commit()

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            include_name=include_name,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


# ---------------------------------------------------------
# Run
# ---------------------------------------------------------

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()