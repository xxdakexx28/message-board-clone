from django.urls import path
from .views import PostlistView

urlpatterns = [
     path("", PostlistView.as_view(), name = "post_list"),
]