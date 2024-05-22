from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('water_list/', WaterListView.as_view(), name='water_list'),
    path('detail/<int:pk>', WaterDetailView.as_view(), name='water-detail'),
    path('delete/<int:pk>', WaterDeleteView.as_view(), name='water-delete'),
    path('create/', WaterCreateView.as_view(), name='water-create'),
    # path('add_review/<int>', AddReviewView.as_view(), name='add-raview'),
    path('category/', CategoriesListView.as_view(), name='category'),
]

