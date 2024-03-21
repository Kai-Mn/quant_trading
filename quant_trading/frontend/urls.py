from django.urls import path
from . import views
from .views import StocksListView, ResultsListView, ResultDetailView, CompaniesListView
from django.conf import settings
from django.conf.urls.static import static


#TODO this isn't DRY
# URLConf
urlpatterns = [
    path('', views.index),
    path('get_stock/', views.get_stock),
    path('stocks/', StocksListView.as_view()),
    path('results/', ResultsListView.as_view()),
    path('companies/', CompaniesListView.as_view(), name='companies'),
    path('results/<int:result_id>', ResultDetailView.as_view(), name='result_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 