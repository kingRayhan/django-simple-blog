from django.conf.urls import url
from django.contrib import admin
from django.urls import conf, path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
Learn Todo
------------------------------------
- Templating
- Static file and media load
- Orm
- Authentication
- Middleware
- Rest Framework and Graphene(Graphql)
- Queue/Event
- Socket
"""