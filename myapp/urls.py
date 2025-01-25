from django.urls import path
from .views import FactoryListView, FactoryDetailView, map_view

urlpatterns = [
    path('factories/', FactoryListView.as_view(), name='factory-list'),
    path('factories/<uuid:pk>/', FactoryDetailView.as_view(), name='factory-detail'),
    path('map/', map_view, name='map')
]