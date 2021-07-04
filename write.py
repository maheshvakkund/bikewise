from util import get_connection
from read import fetch_bikes_data


def write_data(db_details):
    bikes_df = fetch_bikes_data()
    SOURCE_DB = db_details['SOURCE_DB']

    connection = get_connection(db_type=SOURCE_DB['DB_TYPE'],
                                db_host=SOURCE_DB['DB_HOST'],
                                db_name=SOURCE_DB['DB_NAME'],
                                db_user=SOURCE_DB['DB_USER'],
                                db_password=SOURCE_DB['DB_PASSWORD'],
                                db_port=SOURCE_DB['DB_PORT'])
    columns_names = ','.join(bikes_df.columns)
    values = ','.join(['%s'] * len(bikes_df.columns))
    save_data(connection, columns_names, values, bikes_df)


def save_data(connection, columns_names, values, dataframes):
    cursor = connection.cursor()
    query = f"INSERT INTO `bikewise_data` ({columns_names}) VALUES({values})"
    cursor.executemany(query, dataframes.values.tolist())
    connection.commit()
    connection.close()

