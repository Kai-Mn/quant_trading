from django.urls import path
from . import views
from .views import StocksListView
from django.conf import settings
from django.conf.urls.static import static

# URLConf
urlpatterns = [
    path('', views.index),
    path('get_stock/', views.get_stock),
    path('stocks/', StocksListView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 