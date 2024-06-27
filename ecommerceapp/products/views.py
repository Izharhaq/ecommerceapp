from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminOrHasEditPermission
from django.shortcuts import render
from django.http import JsonResponse   

class ProductListView(generics.ListAPIView):        #GET Method
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]

class ProductDetailView(generics.RetrieveAPIView):      #GET Method
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]

class ProductCreateView(generics.CreateAPIView):    # POST Method
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]


class ProductUpdateView(generics.UpdateAPIView):     # PUT Method
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]

class ProductDeleteView(generics.DestroyAPIView):   # DELETE Method
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHasEditPermission]



######################
'''
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateUpdateRetrieveDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk:
            # Retrieve a single product
            try:
                product = Product.objects.get(pk=pk)
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            # List all products
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        # Create a new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        # Update an existing product
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # Delete a product
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

'''


################
# def product_list(request):
#     return render(request, 'products/product_list.html', context={})

def json_view(request):
    # This will render the HTML template
    return render(request, 'templates/json_template.html')

def fetch_products(request):
    # Simulated JSON data representing saved products
    products = [
        {
            "id": 1,
            "name": "watch",
            "description": "smart watch",
            "price": "10000.00",
            "stock": 10,
            "created_at": "2024-06-25T13:13:08.997991Z",
            "updated_at": "2024-06-25T13:13:08.998015Z",
            "owner": None
        }
        # Add more products if needed
    ]
    return JsonResponse(products, safe=False)