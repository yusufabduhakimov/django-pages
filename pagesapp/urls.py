from django.urls import path
from .views import HomePageView, AboutPageView, DamirPageView, method

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('Damir/', DamirPageView.as_view(), name='damir'),
    path('method/', method, name='method'),
]
