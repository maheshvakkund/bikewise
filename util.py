import pandas as pd


def get_tables(path):
    tables_df = pd.read_csv(path, sep=':')
    return tables_df.query('to_be_loaded == "yes"')