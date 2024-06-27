from django.urls import path
from .views import ProductListView, ProductUpdateView
from .views import json_view, fetch_products


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),      # To get list and add products
    path('<int:pk>/', ProductListView.as_view(), name='products_list'),     #To get a product detail
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),  #To upadte or delete a product with pk
    path('json/', json_view, name='json_view'),
    path('api/products/', fetch_products, name='fetch_products'),

]
