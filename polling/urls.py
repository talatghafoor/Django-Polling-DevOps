
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from polls import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='polls/', permanent=True)),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
