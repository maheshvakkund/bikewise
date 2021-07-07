import requests
import json
import pandas as pd


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
