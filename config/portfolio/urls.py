from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.get_portfolio, name='get_portfolio'),
]