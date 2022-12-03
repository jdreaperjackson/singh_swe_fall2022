# URL mappings for the application
from django.urls import path
from . import views

# Define the namespace for the sd_app.
app_name = "sd_app"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('profile/', views.profilePage, name = 'profile'),
    path('buy/', views.buyPage, name='buy'),
    path("register/", views.registerPage, name="register"),
    path('purchase_history/', views.purchaseHistoryPage, name='purchase_history'),

    ]