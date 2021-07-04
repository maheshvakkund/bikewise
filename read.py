from util import get_connection
import requests
import json
import pandas as pd


def read_table(db_details, table_name, limit=0):
    SOURCE_DB = db_details['SOURCE_DB']
    connection = get_connection(db_type=SOURCE_DB['DB_TYPE'],
                                db_host=SOURCE_DB['DB_HOST'],
                                db_name=SOURCE_DB['DB_NAME'],
                                db_user=SOURCE_DB['DB_USER'],
                                db_password=SOURCE_DB['DB_PASSWORD'],
                                db_port=SOURCE_DB['DB_PORT'])
    cursor = connection.cursor()
    if limit == 0:
        query = f'SELECT * FROM {table_name}'
    else:
        query = f'SELECT * FROM {table_name} LIMIT {limit}'
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = cursor.column_names
    connection.close()
    return data, column_names


def fetch_bikes_data():
    payload = json.loads(
        requests.get('https://bikewise.org:443/api/v2/incidents').content.decode('utf-8'))['incidents']
    bikes_df = pd.json_normalize(payload)
    bikes_df = bikes_df[['id',
                         'title',
                         'description',
                         'address',
                         'occurred_at',
                         'updated_at',
                         'url',
                         'location_type',
                         'location_description',
                         'type',
                         'type_properties',
                         'source.name',
                         'source.html_url',
                         'source.api_url']].rename(columns={'source.name': 'source_name',
                                                            'source.html_url': 'source_html_url',
                                                            'source.api_url': 'source_api_url'})
    return bikes_df
