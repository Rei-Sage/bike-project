from django.urls import path , include
from workspace import views
from .views import *
urlpatterns = [
    path('create',views.create_bike,name='create_bike'),
    path('update/<int:id>/', views.update_bike, name='update_bike'),
    path('news/delete/<int:id>/', views.delete, name='delete'),
    path('', views.main, name='workspace'),
]