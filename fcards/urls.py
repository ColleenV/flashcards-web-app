from django.conf.urls import patterns, url
from fcards import views
from .views import Subject

urlpatterns = patterns('',

        url(r'^index/$', views.index, name='index'),
        url(r'^$', views.index, name='index'),
        url(r'^main/$', views.main, name='main'),
        url(r'^new/$', views.card_new, name='card_new'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'(?P<name>\w+)/$', views.Subject, name='subject'),
        )
