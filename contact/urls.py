from django.conf.urls import url, include
from . import views

urlpatterns = [
url(r'^$', views.contact, name='contact'),
url(r'^success/$', views.success, name='success'),
]