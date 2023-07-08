python_sources()


pex_binary(
    name="uvicorn",
    entry_point="app.py",
    dependencies=[
        '//:poetry#asyncpg',
        '//:poetry#greenlet',
    ],
    restartable=True,
)

pex_binary(
    name="alembic",
    script="alembic",
    dependencies=[
        "//:poetry#alembic",
        '//:poetry#fastapi',
        '//:poetry#uvicorn',
        '//:poetry#psycopg2',
        '//:poetry#asyncpg',
        '//:poetry#greenlet',
    ],
)

# pex_binary(
#     name='alembic',
#     entry_point='alembic.config:main',
#     dependencies=[
#         '//:poetry#alembic',
#         '//:poetry#fastapi',
#         '//:poetry#uvicorn',
#         '//:poetry#psycopg2',
#         '//:poetry#asyncpg',
#         '//:poetry#greenlet',
#     ],
#     output_path='projects/mewt_backend'
# )

# sources=['alembic.ini'],
#     sources=['migrations'],