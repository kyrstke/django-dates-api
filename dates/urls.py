from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_post_dates),
    path('<int:pk>/', views.delete_date),
]