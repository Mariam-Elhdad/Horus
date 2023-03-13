from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.views import View
from rest_framework import generics
from rest_framework.views import APIView

from .permissions import CreatorOrReadOnlyPermission, PostIfCreatorPermission
from horus.blog.models import ABCVoting, Downvote, Love, Post, Comment, Upvote
from .serializers import BasePostSerializer, CommentFullDataSerializer, DownVoteSerializer, LoveSerializer, PostSerializer, CommentSerializer, CommentCreateSerializer, ReplyCreateSerializer, ReplySerializer, UpVoteSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostObject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CreatorOrReadOnlyPermission,)


class CommentList(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    


class CommentObject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentFullDataSerializer
    permission_classes = (CreatorOrReadOnlyPermission,)


class ReplyList(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ReplyCreateSerializer
    


class ReplyObject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = ReplySerializer
    permission_classes = (CreatorOrReadOnlyPermission,)

class LoveView(generics.CreateAPIView):
    queryset = Love.objects.all()
    serializer_class = LoveSerializer

    @classmethod
    def check_valition_data(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

    @classmethod
    def get_comment(self, request):
        return get_object_or_404(Comment, id=request.data['comment_id'])

    def post(self, request):
        self.check_valition_data(request)
        comment = self.get_comment(request)
        creator = request.user
        
        love = Love.objects.filter(comment=comment, creator=creator)
        
        if love:
            love.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        Love.objects.create(comment_id=comment.id, creator_id=creator.id)
        return Response(status=status.HTTP_200_OK)


class VotingManager(APIView):
    serializer_class = UpVoteSerializer
    model = Upvote

    @classmethod
    def check_valition_data(cls, request):
        serializer = cls.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

    @classmethod
    def get_post(cls, request) -> Post:
        post_id = request.data['post_id']
        return get_object_or_404(Post, id=post_id)
    
    @classmethod
    def get_voter(cls, request) -> Post:
        voter_id = request.data['voter_id']
        return get_object_or_404(User, id=voter_id)

    @classmethod
    def normalizer_for_related(cls, post, voter, model: ABCVoting):
        print(model)
        try:
            return model.objects.get(post=post, voter=voter)
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_up_down_vote(cls, post, voter):
        return cls.normalizer_for_related(post, voter, Upvote), cls.normalizer_for_related(post, voter, Downvote)
    
    @classmethod
    def perform_post_voting(cls, obj: ABCVoting, post: Post, voter:User, successed_created: str, successed_removed: str, rev: ABCVoting):
        if obj is None:
            if rev:
                rev.delete()
            obj = cls.model.objects.create(post=post, voter=voter)
            return Response({'detail': successed_created}, status=status.HTTP_201_CREATED)

        obj.delete()
        return Response({'detail': successed_removed}, status=status.HTTP_204_NO_CONTENT)


class UpAndUnVote(VotingManager):
    serializer_class = UpVoteSerializer
    model = Upvote

    def post(self, request):
        self.check_valition_data(request)
        post = self.get_post(request)
        voter = request.user
        
        upvote, downvote = self.get_up_down_vote(post, voter)

        return self.perform_post_voting(upvote, post, voter, successed_created='upvoted',
                        successed_removed='un upvoted', rev=downvote)


class DownAndUnVote(VotingManager):
    serializer_class = DownVoteSerializer
    model = Downvote

    def post(self, request):
        self.check_valition_data(request)
        post = self.get_post(request)
        voter = request.user
        upvote, downvote = self.get_up_down_vote(post, voter)
        return self.perform_post_voting(downvote, post, voter, successed_created='downvoted',
                        successed_removed='un downvoted', rev=upvote)


class VotingState(APIView):
    def get(self, request):
        user = request.user
        post_id = request.data.get('post_id')
        if post_id is None:
            return Response({'detail': 'you should send post_id'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Post.objects.filter(id=request.data['post_id']).count():
            post = Post.objects.get(id=request.data['post_id'])
            if Upvote.objects.filter(voter=user, post=post).exists():
                return Response({'state': 'upvote'})
            if Downvote.objects.filter(voter=user, post=post).exists():
                return Response({'state': 'downvote'})
        else:
            return Response({'detail': 'post not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'state': ''})
    