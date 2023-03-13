from django.contrib import admin
from .models import Downvote, Post, Comment, Upvote


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['creator', 'title', 'content', 'tags']


class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'body', 'post']


class VotingAdmin(admin.ModelAdmin):
    fields = ['post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Upvote, VotingAdmin)
admin.site.register(Downvote, VotingAdmin)
