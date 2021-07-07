import os
from util import get_spark_session
from read import fetch_bikes_data


def start_application():
    env = os.environ.get('ENVIRON')
    spark = get_spark_session(env, 'Bikewise Activity')
    spark.sql("SELECT current_date()").show()
    fetch_bikes_data()


if __name__ == '__main__':
    start_application()
