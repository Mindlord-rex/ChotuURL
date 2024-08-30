from django.urls import path
from .views import home_view, redirect_view

app = 'main'

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:short_part>/', redirect_view, name='redirect')
]
