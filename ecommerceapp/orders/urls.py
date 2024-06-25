from django.urls import path
from .views import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('list/', OrderListView.as_view(), name='orders_list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('add/', OrderCreateView.as_view(), name='add_order'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete_order'),

]
