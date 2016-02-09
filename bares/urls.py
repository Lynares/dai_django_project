# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from bares import views
# Aqui anñadimos las urls
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^bar/(?P<bar_nombre_slug>[\w\-]+)/$', views.bar, name='bar'),
        url(r'^bar/(?P<bar_nombre_slug>[\w\-]+)/add_tapas/$', views.add_tapas, name='add_tapas'),
        url(r'^register/$', views.register, name='register'), # Para el registro de usuarios
        url(r'^login/$', views.user_login, name='login'), # Para el login de usuarios
        url(r'^logout/$', views.user_logout, name='logout'), # Para el login de usuarios
        url(r'^restricted/$', views.restricted, name='restricted'), # Para el acceso a partes solo de usuarios
        url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'), # Para el login de usuarios
        )
