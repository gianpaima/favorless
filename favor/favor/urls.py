from django.conf.urls import patterns, include, url
#Settings
from django.conf import settings
#finSetting
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'favor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'registro_usuarios.views.home', name='home'),
    url(r'^$', 'registro_usuarios.views.home', name='home'),
    url(r'^login/$', 'registro_usuarios.views.iniciarSesion', name='login'),
    url(r'^principal/$', 'registro_usuarios.views.principal', name='principal'),
    url(r'^signup/$', 'registro_usuarios.views.registrarUsuarioInicio', name='signup'),
    url(r'^signup/validar/$', 'registro_usuarios.views.validar', name='validar'),
    url(r'^account/create/$', 'registro_usuarios.views.registrarUsuarioFin', name='account/create/'),
    url(r'^logout/$', 'registro_usuarios.views.cerrarSesion', name='logout'),
    url(r'^preferencias/$', 'registro_usuarios.views.preferencias', name='preferencias'),
    url(r'^addpreference/$', 'registro_usuarios.views.addpreference', name='addpreference'),
   # url(r'^preferenciasajax/$', 'registro_usuarios.views.preferenciasajax', name='preferenciasajax'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,} 
		),
    url(r'^admin/', include(admin.site.urls)),

)
