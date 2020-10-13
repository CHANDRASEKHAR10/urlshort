from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100,null=True)
    content = models.TextField()
    author = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    titlec = models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)

class Replies(models.Model):
    reptocomment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)
    reply = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)



