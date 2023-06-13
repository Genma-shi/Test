# BOT settings
TOKEN = "6130718473:AAFOymA1PdGECQuau5NrjgFqedYILmbHb48"
ADMINS_IDS = []


# DATABASE settings
POSTGRES_USER = "bot_user"
POSTGRES_PASSWORD = "dastan150506"
POSTGRES_DATABASE = "lunch_bot_db"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432

POSTGRES_URL = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}".format(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    name=POSTGRES_DATABASE
)