import sys
from config import DB_DETAILS
from util import get_tables


def print_hi(name):
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)
    tables_df = get_tables('tables_list.txt')
    for table in tables_df['table_name']:
        print(table)


if __name__ == '__main__':
    print_hi('PyCharm')
