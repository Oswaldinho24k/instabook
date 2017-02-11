from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accUrls

from django.conf import settings
from django.views.static import serve

urlpatterns = [
	

    url(r'^admin/', admin.site.urls),
    url(r'^', include(accUrls)), 

     url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
