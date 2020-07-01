from django.urls import re_path, path, include
from .views import Index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', Index.as_view(), name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

