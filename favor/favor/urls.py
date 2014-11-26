<<<<<<< HEAD

=======
>>>>>>> 9f9b5b8474ac5c2edbc0b5d0c96af2a1703d5917
from django.conf.urls import patterns, include, url
#Settings
from django.conf import settings
#finSetting
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
    # Examples:
    # url(r'^$', 'favor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'registro_usuarios.views.home', name='home'),
    url(r'^$', 'registro_usuarios.views.home', name='home'),
    url(r'^login/$', 'registro_usuarios.views.iniciarSesion', name='login'),
    url(r'^signup/$', 'registro_usuarios.views.registrarUsuario', name='signup'),
    url(r'^principal/$', 'registro_usuarios.views.principal', name='principal'),
    url(r'^logout/$', 'registro_usuarios.views.cerrarSesion', name='logout'),
    url(r'^principal/preferencias/$', 'registro_usuarios.views.preferencias', name='preferencias'),
     url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,} 
		),
    url(r'^admin/', include(admin.site.urls)),
=======
# Examples:
# url(r'^$', 'favor.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
#url(r'^$', 'registro_usuarios.views.home', name='home'),
url(r'^$', 'registro_usuarios.views.home', name='home'),
url(r'^login/$', 'registro_usuarios.views.iniciarSesion', name='login'),
url(r'^signup/$', 'registro_usuarios.views.registrarUsuario', name='signup'),
url(r'^principal/$', 'registro_usuarios.views.principal', name='principal'),
url(r'^logout/$', 'registro_usuarios.views.cerrarSesion', name='logout'),
url(r'^media/(?P<path>.*)$','django.views.static.serve',
{'document_root':settings.MEDIA_ROOT,}
),
url(r'^admin/', include(admin.site.urls)),
>>>>>>> 9f9b5b8474ac5c2edbc0b5d0c96af2a1703d5917
)
