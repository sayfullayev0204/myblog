from django.urls import path
from .views import index,code,save_location


urlpatterns = [
    path('', index, name='index'),
    path('code/', code, name='code'),
    path('save_location/', save_location, name='save_location'),


]