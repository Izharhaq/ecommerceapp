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
'''
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
'''
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer



class OrderListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]

    def get(self, request, order_no=None, format=None):
        if order_no:
            # Retrieve a single product
            try:
                order = Order.objects.get(order_no=order_no)
                serializer = OrderSerializer(order)
                return Response(serializer.data)
            except Order.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            # List all orders
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)


    def post(self, request, format=None):
        # Create a new order
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]

    def put(self, request, order_no, format=None):
        # Update an existing order
        try:
            order = Order.objects.get(order_no=order_no)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_no, format=None):
        # Delete an order
        try:
            order = Order.objects.get(order_no=order_no)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)