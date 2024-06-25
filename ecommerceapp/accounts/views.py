from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model, login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from .models import CustomUser

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # def admin_login(request):
    #     return render(request, 'accounts/admin_login.html')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            if user.is_superuser:
                return redirect('superadmin_dashboard')
            elif user.is_subuser:
                return redirect('subuser_dashboard')
            else:
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class SuperadminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'accounts/superadmin_dashboard.html'
    
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super().handle_no_permission()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subusers'] = User.objects.filter(is_subuser=True)
        return context

class SubuserDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'accounts/subuser_dashboard.html'

    def test_func(self):
        return self.request.user.is_subuser

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super().handle_no_permission()
