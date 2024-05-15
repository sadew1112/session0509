from django.urls import path, include
from .views import *

app_name = 'posts'

urlpatterns = [
    # path('post/', PostAPIView.as_view()),
    # path('post/', PostAPIView2.as_view()),
    path('post/', PostAPI_FBV), # 추가
    path('list/', Postlist_CBV.as_view()),
    path('comment/', Postcomment_CBV.as_view()),
]