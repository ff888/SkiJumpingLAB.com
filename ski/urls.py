from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fantasy-league/', views.fantasy_league, name='fantasy-league'),
    path('live/', views.live, name='live'),
    path('statistics/', views.statistics, name='statistics'),
    path('blog/', views.blog, name='blog'),
]