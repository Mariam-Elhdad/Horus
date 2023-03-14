from django.urls import path

from .api.views import (
    CommentList,
    CommentObject,
    DownAndUnVote,
    LoveView,
    PostList,
    PostObject,
    ReplyList,
    ReplyObject,
    UpAndUnVote,
    VotingState,
)

urlpatterns = [
    path("", PostList.as_view()),
    path("<int:pk>/", PostObject.as_view()),
    path("comments/", CommentList.as_view()),
    path("comments/<int:pk>/", CommentObject.as_view()),
    path("comments/reply/", ReplyList.as_view()),
    path("comments/reply/<int:pk>/", ReplyObject.as_view()),
    path("comments/love/", LoveView.as_view()),
    path("upvote/", UpAndUnVote.as_view()),
    path("downvote/", DownAndUnVote.as_view()),
    path("voting_state/", VotingState.as_view()),
]
