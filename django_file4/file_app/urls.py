from django.urls import path


from .views import *


urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
    path('get_file/<int:pk>/', get_file, name='get_file'),
]
