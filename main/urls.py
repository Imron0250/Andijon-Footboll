from django.urls import path
from .views import *

urlpatterns = [
    path('get-info/', get_info),
    path('get-main-page/', get_main_page),
    path('get-news/', get_news),
    path('get-media/', get_media),
    path('get-statistics/', get_statistics),
    path('get-info-about_players/', get_info_about_players),
    path('get-about-academy/', get_about_academy),
]
