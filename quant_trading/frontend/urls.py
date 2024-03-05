from django.urls import path
from . import views
from .views import StocksListView

# URLConf
urlpatterns = [
    path('', views.index),
    path('get_stock/', views.get_stock),
    path('stocks/', StocksListView.as_view())
]