from django.urls import path, include
from .views import searchAPI
from .views import saveVideo

urlpatterns = [
    path("find", searchAPI),
    path('save/', saveVideo),  #<str:youtube_url>
    # path('stream/<str:video_id>', streamVideo),

]