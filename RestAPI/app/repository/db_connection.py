import pyodbc
from app.core.config import settings


def get_db_connection():
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={settings.DB_SERVER};"
        f"DATABASE={settings.DB_DATABASE};"
        f"Trusted_Connection=yes;"
    )

    return pyodbc.connect(connection_string)

