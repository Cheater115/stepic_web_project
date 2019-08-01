from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^question/<?P<question_id>\d+/$', views.test, 'question'),
    url(r'^login/$', views.test, 'login'),
    url(r'^signup/$', views.test, 'signup'),
    url(r'^ask/$', views.test, 'ask'),
    url(r'^popular/$', views.test, 'popular'),
    url(r'^new/$', views.test, 'new'),
]