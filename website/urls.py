from django.conf.urls import url
from django.contrib import admin
from Books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='book'),
    # url(r'^/$', views.search, name='search'),
    url(r'^/$', views.BookSearchView.as_view(), name='search'),
    url(r'^donate/$', views.donatePage, name='donate'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)