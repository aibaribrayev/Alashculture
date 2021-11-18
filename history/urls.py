from django.urls import path
from . import views

urlpatterns = [
    path('', views.allhistory, name='allhistory'),
]
