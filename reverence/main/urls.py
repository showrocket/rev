from .views import CatalogView, ClothingItenDetailView
from django.urls import path


app_name = 'main'

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('item/<slug:slug>/', ClothingItenDetailView.as_view(),
         name='clothing_item_detail')
]
