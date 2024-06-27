from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views import json_view, fetch_products


urlpatterns = [
    path('list/', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', ProductCreateView.as_view(), name='add_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('json/', json_view, name='json_view'),
    path('api/products/', fetch_products, name='fetch_products'),

]


##########
'''
from django.urls import path
from .views import ProductListCreateUpdateRetrieveDeleteAPIView

urlpatterns = [
    path('products/', ProductListCreateUpdateRetrieveDeleteAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductListCreateUpdateRetrieveDeleteAPIView.as_view(), name='product-detail-update-delete'),
]

'''