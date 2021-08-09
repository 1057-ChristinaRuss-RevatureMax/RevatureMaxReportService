# routes need to be touched by import once to proc the app import/setup
# from src.config.db_config import execute_sql
from src.route import *
from src.config.flask_config import app
from dotenv import dotenv_values


if __name__ == "__main__":
    dotenv_values("../.env")
    app.run(host="0.0.0.0")
    # execute_sql("src/sql/setup.sql")
