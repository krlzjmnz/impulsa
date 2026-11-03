import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=int(os.getenv("DB_PORT", "3306"))
        )

        if connection.is_connected():
            print("---------")
            return connection

    except Error as e:
        print("Error al conectar a MySQL:", e)

    return None


def cerrar(connection):
    if connection is not None and connection.is_connected():
        connection.close()