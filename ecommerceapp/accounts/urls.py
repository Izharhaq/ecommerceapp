from django.urls import path
from .views import RegisterView, LoginView, SuperadminDashboardView, SubuserDashboardView

urlpatterns = [
    
    path('login/', LoginView.as_view(), name='admin_login'),
    path('superadmin/', SuperadminDashboardView.as_view(), name='superadmin_dashboard'),
    path('subuser/', SubuserDashboardView.as_view(), name='subuser_dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
]


