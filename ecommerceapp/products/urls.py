from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', ProductCreateView.as_view(), name='add_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

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