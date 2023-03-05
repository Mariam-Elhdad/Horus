from django.urls import path

from .api.views import DownAndUnVote, PostList, PostObject, CommentList, CommentObject, ReplyList, ReplyObject, TagPosts, \
    Tagging, UnTagging, UpAndUnVote, LoveView, VotingState

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostObject.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentObject.as_view()),
    path('comments/reply/', ReplyList.as_view()),
    path('comments/reply/<int:pk>/', ReplyObject.as_view()),
    path('comments/love/', LoveView.as_view()),
    path('tags/', Tagging.as_view()),
    path('tags/<str:name>/delete/', UnTagging.as_view()),
    path('tags/<str:name>/', TagPosts.as_view()),
    path('upvote/', UpAndUnVote.as_view()),
    path('downvote/', DownAndUnVote.as_view()),
    path('voting_state/', VotingState.as_view()),
]
