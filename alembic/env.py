import os
import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool
from alembic import context
from dotenv import load_dotenv

# Importar la clase Base y los modelos de tu backend
from caja_de_ahorros_backend import Base, Socio, Cuenta, Asiento

# Cargar las variables del archivo .env
load_dotenv()

config = context.config

# Configurar el logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Configurar la URL de conexión desde el .env
raw_url = os.getenv("DATABASE_URL")
if raw_url and "?sslmode=require" in raw_url:
    raw_url = raw_url.replace("?sslmode=require", "")
    
config.set_main_option("sqlalchemy.url", raw_url)
target_metadata = Base.metadata

def do_run_migrations(connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())

# Ejecutar las migraciones
run_migrations_online()