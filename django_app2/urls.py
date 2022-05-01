from django.conf.urls import url
from django_app2 import views

urlpatterns = [
    url(r'^$',views.help,name='help'),
]
