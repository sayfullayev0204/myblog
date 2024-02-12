from django.urls import path
from .views import index,code


urlpatterns = [
    path('', index, name='index'),
    path('code/', code, name='code')

]