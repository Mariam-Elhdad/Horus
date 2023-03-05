from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from horus.blog.models import Love, Post, Comment, Reply, Tag, Upvote
from django.contrib.auth.models import User


class UserTextBaseSerializer(serializers.ModelSerializer):
    date_posted = serializers.DateTimeField(format='%Y-%d-%m %H:%M:%S', read_only=True)
    id = serializers.IntegerField(read_only=True)
    creator_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        abstract = True

    def get_creator_id(self, obj):
        creator = obj.creator
        return creator.id

    

class ReplyCreateSerializer(serializers.ModelSerializer):
    comment_id = serializers.IntegerField()

    class Meta:
        model = Reply
        fields = ['body', 'comment_id']

    # def create(self, validated_data):
    #     comment = get_object_or_404(Comment, pk=validated_data['comment_id'])
    #     creator = self.context['request'].user
    #     instance = Reply(commen=comment, creator=creator, **validated_data)
    #     instance.save()
    #     return instance

class ReplySerializer(UserTextBaseSerializer):

    class Meta:
        model = Reply
        fields = ['id', 'body', 'date_posted', 'creator_id']


class LoveSerializer(serializers.ModelSerializer):
    comment_id = serializers.IntegerField()
    creator_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Love
        fields = ['comment_id', 'creator_id']



class CommentCreateSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ['body', 'post_id']

    def create(self, validated_data):
        post = get_object_or_404(Post, pk=validated_data['post_id'])
        creator = self.context['request'].user
        instance = Comment(post=post, creator=creator, **validated_data)
        instance.save()
        return instance

        

class CommentSerializer(UserTextBaseSerializer):
    
    class Meta:
        model = Comment
        fields = ['id', 'body', 'date_posted', 'creator_id']


    

class CommentFullDataSerializer(UserTextBaseSerializer):
    replies = serializers.SerializerMethodField(read_only=True)
    loves = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'body', 'date_posted', 'creator_id', 'replies', 'loves']

    
    def get_replies(self, obj: Comment):
        replies = obj.comment_reply.all()
        return ReplySerializer(replies, many=True).data
    
    def get_loves(self, obj: Comment):
        return obj.comment_love.count()
    


class BasePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content']


class PostSerializer(UserTextBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    date_posted = serializers.DateTimeField(format='%Y-%d-%m', read_only=True)
    comments_number = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    tags = serializers.SerializerMethodField(read_only=True)
    creator_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'creator_id', 'title', 'content', 'date_posted', 'comments_number', 'upvotes', 'downvotes',
                    'comments', 'tags']

    
    def create(self, validated_data):
        creator = self.context['request'].user
        instance: Post = Post(creator=creator, **validated_data)
        instance.save()
        return instance

    

    def get_comments_number(self, obj: Post):
        return obj.post_comments.count()

    def get_comments(self, obj: Post):
        comments = obj.post_comments.all()
        return CommentSerializer(comments, many=True).data

    def get_tags(self, obj: Post):
        tags = obj.post_tags.all()
        return TagSerializer(tags, many=True).data
    



class TaggingPostCreationSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(write_only=True) 
    name = serializers.CharField(max_length=100, write_only=True)
    
    class Meta:
        model = Tag
        fields = ['post_id', 'name']

    def create(self, validated_data):
        name = validated_data['name']
        post_id = validated_data['post_id']

        tag, is_created = Tag.objects.get_or_create(name=name)
        post = get_object_or_404(Post, id=post_id)
        tag.post.add(post)
        return tag

    




class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)
    
   

class TagPostsSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tag
        fields = ('name', 'posts')
    
    def get_posts(self, obj: Tag):
        posts = obj.post.all()
        return BasePostSerializer(posts, many=True).data


class ABCVotingSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField()

    class Meta:
        model = Upvote
        fields = ('post_id',)
        
    
class UpVoteSerializer(ABCVotingSerializer):
    pass


class DownVoteSerializer(ABCVotingSerializer):
    pass
