from django.db import models
from taggit.managers import TaggableManager

from horus.users.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_posts", default=1
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    date_last_update = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    @property
    def creator_id(self):
        return self.creator.id

    @property
    def upvotes(self):
        return self.post_upvote.all().count()

    @property
    def downvotes(self):
        return self.post_downvote.all().count()

    def __str__(self):
        return self.title


class CommentBase(models.Model):
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(CommentBase):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comments"
    )
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments", default=1
    )

    def __str__(self):
        return f"{self.id} -> {self.post}"


class Love(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="comment_love"
    )
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_love"
    )

    def __str__(self) -> str:
        return f"love from {self.creator.id} on commment {self.comment.id}"


class Reply(CommentBase):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="comment_reply"
    )
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reply", default=1
    )

    def __str__(self):
        return f"{self.id} -> {self.comment}"


class ABCVoting(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"post:{self.post}, voter:{self.voter}"


class Upvote(ABCVoting):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_upvote")
    voter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="voter_upvote", default=1
    )


class Downvote(ABCVoting):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_downvote"
    )
    voter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="voter_downvote", default=1
    )
