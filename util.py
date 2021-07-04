import pandas as pd
from mysql import connector as mc
from mysql.connector import errorcode as ec
from config import DB_DETAILS
import psycopg2


def get_tables(path):
    tables_df = pd.read_csv(path, sep=':')
    return tables_df.query('to_be_loaded == "yes"')


def get_mysql_connection(db_host, db_name, db_user, db_password, db_port):
    try:
        connection = mc.connect(host=db_host,
                                database=db_name,
                                user=db_user,
                                password=db_password,
                                port=db_port)
    except mc.connector.Error as err:
        if err.errno == ec.ER_ACCESS_DENIED_USER:
            print("Invalid credentials")
        else:
            print("Error")
    return connection


def get_pg_connection(db_host, db_name, db_user, db_password, db_port):
    """
        This Method returns a new Connection object for every request, if unable to create a connection object,
        it will throw an Exception.
    """
    connection = None
    try:
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_name,
            password=db_password
        )
    except Exception as e:
        raise e

    return connection


def get_connection(db_type, db_host, db_name, db_user, db_password, db_port):
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host=db_host,
                                          db_name=db_name,
                                          db_user=db_user,
                                          db_password=db_password,
                                          db_port=db_port)
    if db_type == 'postgres':
        connection = get_pg_connection(db_host=db_host,
                                       db_name=db_name,
                                       db_user=db_user,
                                       db_password=db_password,
                                       db_port=db_port)
    return connection


def load_db_details(env):
    return DB_DETAILS[env]
