from django.urls import path
from .views import OrderListView, OrderUpdateView

urlpatterns = [

    path('', OrderListView.as_view(), name='orders_list'),      # To get list and add products
    path('<str:order_no>/', OrderListView.as_view(), name='orders_detail'),     #To get a product detail
    path('update/<str:order_no>/', OrderUpdateView.as_view(), name='update_order'),  #To upadte or delete a product with pk

]
