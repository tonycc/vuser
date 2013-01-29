from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vuser.views.home', name='home'),
    # url(r'^vuser/', include('vuser.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'vuser.sinaweibo.views.index',name=""),
    url(r'^index/$','vuser.sinaweibo.views.index',name='index'),
    url(r'^login/$','vuser.sinaweibo.views.login',name='login'),
    url(r'^login_check/$','vuser.sinaweibo.views.login_check',name="logincheck"),
    url(r'^getfans/$','vuser.sinaweibo.views.get_fans',name="getfans"),
    url(r'^userinfo/$','vuser.sinaweibo.views.get_userinfo',name="userinfo"),

)
