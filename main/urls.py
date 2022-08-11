from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('getAge', views.getAge, name='getAge'),
    path('sendFeedBack', views.sendFeedBack, name='sendFeedBack'),
    path('thankyou', views.thankyou),
]
