from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Image,Comment,Likes,Location,Rider,Driver,UsabilityRating,EngineRating,BodyRating

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewsLetterForm(forms.Form):
  your_name = forms.CharField(label = 'First Name',max_length = 30)
  email = forms.EmailField(label='Email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['posted_on','likes','profile','details','rating','user',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'comment' ]

class EngineForm(forms.ModelForm):
    class Meta:
        model = EngineRating
        fields = ['rating',]


class UsabilityForm(forms.ModelForm):
    class Meta:
        model = UsabilityRating
        fields = ['rating', ]


class BodyForm(forms.ModelForm):
    class Meta:
        model = BodyRating
        fields = ['rating', ]
