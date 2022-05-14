from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_post_date, name='get-post-date'),
    path('<int:pk>/', views.delete_date, name='delete-date'),
]