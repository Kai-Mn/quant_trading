# from quant_trading import celery_app
import yfinance as yf
from django.conf import settings
from frontend.models import Stocks
from sqlalchemy import create_engine

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

data = yf.download("AAPL", period="5d")
data.to_sql('frontend_stocks',engine,if_exists='replace')
