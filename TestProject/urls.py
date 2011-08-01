from django.conf.urls.defaults import patterns, include, url
from django.views.generic import list_detail
from TestProject.views import *
from TestProject.books.views import *
from TestProject.contact.views import *
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TestProject.views.home', name='home'),
    # url(r'^TestProject/', include('TestProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d+)/$', hours_ahead),
    (r'^hello/$', hello),
    (r'^display/$', display_meta),
    (r'^books/search/$', search),
    (r'^books/publishers/$', list_detail.object_list, publisher_info),
    (r'^books/books/$', list_detail.object_list, book_info),
    (r'^books/books/(\w+)/$', books_by_publisher),
    (r'^books/authors/(?P<author_id>\d+)/$', author_detail),
)
