from . import views
from django.urls import path

urlpatterns = [
    path('accounts/', views.login, name='login'),
]