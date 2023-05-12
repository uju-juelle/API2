from django.urls import path
from .views import *

urlpatterns = [
    # path("", api_homepage.as_view(), name="home"),
    # path("<int:id>/detail/", api_detailpage.as_view(), name="detail"),
    path("comments/", api_commenthome.as_view(), name="commenthome"),
    path("<int:id>/commentdetail/", api_commentdetail.as_view(), name="detail"),
]
