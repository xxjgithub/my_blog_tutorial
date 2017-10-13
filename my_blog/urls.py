from django.conf.urls import patterns, include, url
from django.contrib import admin
from article import views
from article.views import RSSFeed

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/',admin.site.urls),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home,name='home'),
	url(r'^(?P<id>\d+)/$', views.detail, name = 'detail'),
	url(r'^archives/$',views.archives,name='archives'),
	url(r'^aboutme/$',views.about_me, name='about_me'),
	url(r'^tag(?P<tag>\w+)/$',views.search_tag, name='search_tag'),
	url(r'^search/$',views.blog_search, name= "search"),
	url(r'^feed/$', RSSFeed(), name = 'RSS'),    #  Add the new urlconf, and set the name to RSS, easy to use in the template url
	
)
