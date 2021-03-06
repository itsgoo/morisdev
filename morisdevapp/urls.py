from django.urls import re_path, path, include
from .views import Index, Portfolio, LiveChat
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', Index.as_view(), name='index'),
    path('portfolio', Portfolio.as_view(), name='portfolio'),
    path('<str:room_name>/', LiveChat.as_view(), name='live_chat'),

]

