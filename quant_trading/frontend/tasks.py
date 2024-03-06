# from quant_trading import celery_app
import yfinance as yf
from django.conf import settings
from frontend.models import Stocks 
from sqlalchemy import create_engine
import time
import datetime

user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']
host = settings.DATABASES['default']['HOST']
port = settings.DATABASES['default']['PORT']

database_url = 'mariadb://{user}:{password}@db:3306/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
)

engine = create_engine(database_url, echo=False)

#TODO make this not hardcoded and asynchronous with cellery or such
data = yf.download("AAPL", period="5d")

# def insert_on_conflict_nothing(table, conn, keys, data_iter):
#     # "a" is the primary key in "conflict_table"
#     data = [dict(zip(keys, row)) for row in data_iter]
#     stmt = insert(table.table).values(data).on_conflict_do_nothing(index_elements=["a"])
#     result = conn.execute(stmt)
#     return result.rowcount
# data.to_sql('stocks', engine, if_exists='append', method=insert_on_conflict_nothing)


# Not able to iterate directly over the DataFrame
# df_records = df.to_dict('records')
# print(type(data.iloc[0].name))
# print(time.mktime(data.iloc[0].name.timetuple()))
# print(data.iloc[0].name)
# breakpoint()

#TODO we are looping over a pd.dataframe here which is an unperformant antipattern. This should be done in SQL
models = []
for index, row in data.iterrows():
    models.append(
        Stocks(
        date=time.mktime(row.name.timetuple()),
        open=row['Open'],
        high=row['High'],
        low=row['Low'],
        close=row['Close'],
        adj_close=row['Adj Close'],
        volume=row['Volume'],
        type_id=1,
        )
    )

# model_instances = [Stocks(
#     date=time.mktime(record.name.timetuple()),
#     open=record['open'],
#     hihg=record['high'],
#     low=record['low'],
#     close=record['close'],
#     adj_close=record['adj_close'],
#     volume=record['volume'],
#     type_id=1,
# ) for record in data]

Stocks.objects.bulk_create(models)
