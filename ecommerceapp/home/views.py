# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework import generics
# from rest_framework.response import Response


# class HomeView(APIView):
#     def get(self, request):
#         return HttpResponse("Welcome to home page")
    
from django.shortcuts import render
from rest_framework.views import APIView

class HomeView(APIView):
    def get(self, request):
        return render(request, 'home.html')
