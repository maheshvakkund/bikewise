import sys
from util import get_tables
from read import read_table
from util import load_db_details


def print_hi(name):
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables = get_tables('tables_list.txt')
    for table_name in tables['table_name']:
        data, column_names = read_table(db_details, table_name+"_data")


if __name__ == '__main__':
    print_hi('PyCharm')
