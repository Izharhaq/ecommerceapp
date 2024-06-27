from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminOrHasEditPermission
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# from .permissions import IsAdminOrIsSubuserOwner
# from django.contrib.auth import get_user_model

# CustomUser = get_user_model()

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]

    # def get_queryset(self):
    #     return Order.objects.filter(customer=self.request.user)
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_admin:
    #         return Order.objects.all()
    #     return Order.objects.filter(customer=user)

    # def perform_create(self, serializer):
    #     serializer.save(customer=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]

    # def get_queryset(self):
    #     return Order.objects.filter(customer=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return Order.objects.all()
        return Order.objects.filter(customer=user)

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]

    def perform_create(self, serializer):
        # user = self.request.user
        # print(f"Creating order by: {user.username}") 
        serializer.save(created_by=self.request.user)

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]


class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]
