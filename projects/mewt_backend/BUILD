python_sources()


pex_binary(
    name="uvicorn",
    entry_point="main.py",
    dependencies=[
        '//:poetry#psycopg2',
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
        '//:poetry#mangum',
    ],
)

python_awslambda(
    name="mewt-backend-lambda",
    runtime="python3.10",
    dependencies=[
        "//:poetry#asyncpg",
        "//:poetry#greenlet",
    ],
    handler="mewt_backend.lambda_handler:handler",
)
