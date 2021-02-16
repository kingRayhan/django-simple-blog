from django.urls import path
from .articles_controllers import index as articles_index, show as articles_show

urlpatterns = [
    path('', articles_index, name='articles.index'),
    path('<slug:title>', articles_show, name='articles.show'),
]
