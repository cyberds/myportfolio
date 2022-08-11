from django.urls import path
from .views import blogHome

urlpatterns = [
    path('', blogHome.as_view(), name='blogHome'),
]

