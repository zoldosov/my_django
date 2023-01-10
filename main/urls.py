from django.urls import path
from .views import index, academy

app_name = 'main'

urlpatterns = [
    path('v1/', index, name='index'),
    path('academy/<int:pk>/', academy, name='academy')
]
