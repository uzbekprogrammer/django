from django.urls import path
from .views import HomePageView, AboutPageVIew


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageVIew.as_view(), name='about')
]