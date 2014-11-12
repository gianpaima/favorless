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
     url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,} 
		),
    url(r'^admin/', include(admin.site.urls)),
)
