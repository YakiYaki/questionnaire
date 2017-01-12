from django.conf.urls import url
from quiz import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^questionnaire$', views.quiz, name="quiz"),
    url(r'^recommends$', views.recs, name="recs"),
    url(r'^contacts', views.contacts, name="contacts")
]
