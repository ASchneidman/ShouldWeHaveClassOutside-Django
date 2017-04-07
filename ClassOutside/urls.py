from django.conf.urls import urls
from ClassOutside import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
