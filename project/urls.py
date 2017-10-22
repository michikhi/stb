from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health
from stb.views import index as stb_index
from stb.views import jjb as stb_jjb
from stb.views import blog as stb_blog
from stb.views import about as stb_about

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^stb/about.html', stb_about),
    url(r'^stb/blog.html', stb_blog),
    url(r'^stb/jjb.html', stb_jjb),
    url(r'^stb/index.html', stb_index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
]
