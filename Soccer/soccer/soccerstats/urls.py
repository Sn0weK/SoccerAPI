from django.urls import path, include
from .views import *



urlpatterns = [
    path('match/<int:id>/', MatchAPIView.as_view()),
    path('match/', MatchListAPIView.as_view()),
    path('match/<int:id>/passes', MatchPassesListAPIView.as_view()),
    path('match/<int:id>/shots', MatchShotsListAPIView.as_view()),
    path('team/<int:id>/', TeamAPIView.as_view()),
    path('team/', TeamListAPIView.as_view()),
    path('player/<int:id>/', PlayerAPIView.as_view()),
    path('player/', PlayerListAPIView.as_view())
]
