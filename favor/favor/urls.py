from django.conf.urls import patterns, include, url
#Settings
from django.conf import settings
#finSetting
from django.contrib import admin

#from registro_usuarios import views
#from votos import views
admin.autodiscover()

handler404 = 'registro_usuarios.views.Error404'
handler500 = 'registro_usuarios.views.Error500'
"""
urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'favor.views.hoHaving said that, you can put this kind of substitution into your javascriptme', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'registro_usuarios.views.home', name='home'),
    ##Voting
    url(r'^votos/$', 'votos.views.home', name='home'),
    url(r'^votos/elegir$', 'votos.views.votar', name='votar'),
    url(r'^versus/$', 'votos.views.versus', name='versus'),
    url(r'^post_versus/$', 'votos.views.post_versus', name='post_versus'),
    url(r'^pages/(?P<slug>[\w-]+)/$', 'votos.views.static_page'),
    url(r'^search/results/$', 'votos.views.resultados'),
    ##Fin voting  -?P<page_alias>.+? (?P<slug>[\w-]+)
    url(r'^$', 'registro_usuarios.views.home', name='home'),
    url(r'^login/$', 'registro_usuarios.views.iniciarSesion', name='login'),
    url(r'^restaurar/$', 'registro_usuarios.views.restaurar', name='login'),
    url(r'^principal/$', 'votos.views.principal', name='principal'),
    url(r'^signup/$', 'registro_usuarios.views.registrarUsuario', name='signup'),
    url(r'^signup/validar/$', 'registro_usuarios.views.validar', name='validar'),
    url(r'^settings/$', 'registro_usuarios.views.configuracionGeneral', name='settings'),
    url(r'^settings/password/$', 'registro_usuarios.views.configuracionPassword', name='settings/password'),
    url(r'^logout/$', 'registro_usuarios.views.cerrarSesion', name='logout'),
    url(r'^preferencias/$', 'registro_usuarios.views.preferencias', name='preferencias'),
    url(r'^addpreference/$', 'registro_usuarios.views.addpreference', name='addpreference'),
    url(r'^pruebaNode/$', 'registro_usuarios.views.pruebaNode', name='pruebaNode'),
    url(r'^pruebarealtime/$', 'registro_usuarios.views.pruebarealtime', name='pruebarealtime'),
    url(r'^removepreference/$', 'registro_usuarios.views.removepreference', name='removepreference'),
    url(r'^search/$', 'registro_usuarios.views.buscarPrograma', name='search'),


    # url(r'^versus/$', 'votos.views.versus', name='versus'),
    # url(r'^post_versus/$', 'votos.views.post_versus', name='post_versus'),

    # url(r'^test/$', 'registro_usuarios.views.test', name='test'),
   # url(r'^preferenciasajax/$', 'registro_usuarios.views.preferenciasajax', name='preferenciasajax'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
		),

    
    url(r'^admin/', include(admin.site.urls)),

)
"""
urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
        ),
    url(r'^admin/', include(admin.site.urls)),
    )
urlpatterns += patterns('registro_usuarios.views',
    url(r'^$', 'home', name='home'),
    url(r'^login/$', 'iniciarSesion', name='login'),
    url(r'^restaurar/$', 'restaurar', name='login'),
    url(r'^signup/$', 'registrarUsuario', name='signup'),
    url(r'^signup/validar/$', 'validar', name='validar'),
    url(r'^settings/$', 'configuracionGeneral', name='settings'),
    url(r'^settings/password/$', 'configuracionPassword', name='settings/password'),
    url(r'^logout/$', 'cerrarSesion', name='logout'),
    url(r'^preferencias/$', 'preferencias', name='preferencias'),
    url(r'^addpreference/$', 'addpreference', name='addpreference'),
    url(r'^pruebaNode/$', 'pruebaNode', name='pruebaNode'),
    url(r'^pruebarealtime/$', 'pruebarealtime', name='pruebarealtime'),
    url(r'^removepreference/$', 'removepreference', name='removepreference'),
    url(r'^search/$', 'buscarPrograma', name='search'),
)

urlpatterns += patterns('votos.views',
    url(r'^principal/$', 'principal', name='principal'),
    url(r'^votos/$', 'home', name='home'),
    url(r'^votos/elegir$', 'votar', name='votar'),
    url(r'^versus/$', 'versus', name='versus'),
    url(r'^post_versus/$', 'post_versus', name='post_versus'),
    url(r'^pages/(?P<slug>[\w-]+)/$', 'static_page'),
    url(r'^search/results/$', 'resultados'),
    url(r'^misvotos/$', 'misVotaciones', name='misVotaciones'),

)
