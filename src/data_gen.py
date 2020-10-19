import random
import uuid
import string
import psycopg2
import pandas as pd
import datetime
from datetime import timedelta
from random import randint
from sqlalchemy import create_engine

# random number generatior
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
# random datetime generatior
def random_date(start, end):
    return start + timedelta(
        seconds=randint(0, int((end - start).total_seconds()))
    )

pk_list = []
id_list = []
title_list = []
description_list = []
pb_timestamp_list = []
lu_timestamp_list = []

for i in range(0,6):
    # pk
    n = random.randint(1,10)
    pk_list.append(n)

    # id
    x = uuid.uuid4()
    id_list.append(str(x)[:256])
    # title
    title_list.append(get_random_string(10))
    # description
    description_list.append(get_random_string(100))
    # published timestamp
    dt = random_date(
        datetime.datetime(year=2018, month=1, day=1),
        datetime.datetime.now()
    )
    pb_timestamp_list.append(str(dt))
    # last update timestamp
    dt = random_date(
        datetime.datetime(year=2020, month=1, day=1),
        datetime.datetime.now()
    )
    lu_timestamp_list.append(str(dt))

apps = {
    'pk':pk_list,
    'id':id_list,
    'title':title_list,
    'description':description_list,
    'published_timestamp':pb_timestamp_list,
    'last_update_timestamp':lu_timestamp_list
    }

print(apps)

# Create a DataFrame
dataFrame = pd.DataFrame(data=apps,
    columns=("pk", "id", "title", "description", "published_timestamp", "last_update_timestamp")
)

print(dataFrame['pk'])
alchemyEngine = create_engine('postgresql+psycopg2://user:pass@localhost:5432/apps')

postgreSQLConnection = alchemyEngine.connect()
postgreSQLTable = "apps"

try:
    frame = dataFrame.to_sql(name=postgreSQLTable, con=postgreSQLConnection, if_exists='replace')
except ValueError as vx:
    print(vx)
except Exception as ex:  
    print(ex)
else:
    print("PostgreSQL Table %s has been created successfully."%postgreSQLTable)
finally:
    postgreSQLConnection.close()
