# -*- encoding: utf-8 -*-
from django.conf.urls import include, url, patterns #Añadido patterns para poder usarlo, 5.4 tutorial
from django.contrib import admin
# Añadido después de crear el directorio media
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'dai_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bares/', include('bares.urls')), # AÑADIDO TUPLA PARA APLICACION BARES 
]

if settings.DEBUG:
    urlpatterns += patterns(
    	'django.views.static',
    	(r'^media/(?P<path>.*)',
    		'serve',
    		{'document_root': settings.MEDIA_ROOT}),
     )
