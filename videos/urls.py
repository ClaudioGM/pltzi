from django.urls import path

from . import api
from . import views

urlpatterns = [
    path('',views.VideoListView.as_view(), name='list'),
    path('<slug:slug>/', views.VideoDetailView.as_view(), name='detail'),
    path('<str:youtube_id>/like', views.like_video, name='likes_video'),
    path('<str:youtube_id>/dislike', views.dislike_video, name='dislikes_video'),
    path('<str:youtube_id>/comment', view=views.comment_video, name='comment_video'),
    path('popular', api.VideoListView.as_view(), name="popular-list"),
    path('popular_ru/<int:id>', api.VideoRU.as_view(), name='video-retrieve-update'),
    path('history', api.VideoHistoryListView.as_view(), name="video-history"),
]
