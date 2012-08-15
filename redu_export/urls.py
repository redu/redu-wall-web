from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redu_export.views.home', name='home'),
    # url(r'^redu_export/', include('redu_export.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redu_csv/', 'fetch_wall.views.redu_csv'),
    url(r'^get_pin/', 'fetch_wall.views.get_pin'),
    url(r'^clear_cookies/', 'fetch_wall.views.clear_cookies'),
    url(r'^show_space/', 'fetch_wall.views.show_space'),
    url(r'^refresh_spaces/','fetch_wall.views.refresh_spaces')

)
