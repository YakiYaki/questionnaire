from django.conf.urls import url
from quiz import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]
