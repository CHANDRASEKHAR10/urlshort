from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class CreateUserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
class Blogform(ModelForm):
    class Meta:
        model=Blog
        fields=['title', 'content']
class Commentform(ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
class Replyform(ModelForm):
    class Meta:
        model=Replies
        fields=['reply']