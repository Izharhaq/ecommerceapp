from django.urls import path
from .views import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/add/', OrderCreateView.as_view(), name='add_user'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='update_user'),
    path('order/delete/<int:pk>/', OrderDetailView.as_view(), name='delete_user'),
    # path('users/find/', UserFind.as_view(), name='find_users'),
]
