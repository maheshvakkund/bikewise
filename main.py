import sys
from config import DB_DETAILS


def print_hi(name):
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)


if __name__ == '__main__':
    print_hi('PyCharm')
