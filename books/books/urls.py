from django.conf.urls import patterns, url



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'books.views.home', name='home'),
    # url(r'^books/', include('books.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
from library.views import searchbook,book,delete,theirbook,add,update,addauthor,form

urlpatterns = patterns('', 
    url(r'^$',book),
    url(r'^search/$',searchbook),
    url(r'^book/$',book),
    url(r'^delete/$',delete),
    url(r'^theirbook/$',theirbook),
    url(r'^add/$',add),
    url(r'^update/$',update),
    url(r'^addauthor/$',addauthor),
    url(r'^form/$',form),
)