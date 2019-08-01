from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^question/(?P<id>\d+)/$', views.question_details, name = 'question'),
    url(r'^login/$', views.test, name = 'login'),
    url(r'^signup/$', views.test, name = 'signup'),
    url(r'^ask/$', views.ask_question, name = 'ask'),
    url(r'^popular/$', views.popular_questions, name = 'popular'),
    url(r'^new/$', views.new_questions, name = 'new'),
    url(r'^$', views.new_questions, name = 'main'),
]