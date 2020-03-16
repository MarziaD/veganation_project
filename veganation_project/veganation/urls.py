from django.urls import path
from veganation import views

app_name = 'veganation'

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('protests/', views.protests, name='protests'),
    path('signup/', views.signup, name='signup'),
    ]