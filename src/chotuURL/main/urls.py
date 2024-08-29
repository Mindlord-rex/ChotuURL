from django.urls import path
from .views import home_view

app = 'main'

urlpatterns = [
    path('', home_view, name='home'),
]
