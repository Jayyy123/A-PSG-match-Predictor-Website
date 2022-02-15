from cProfile import label
from mimetypes import init
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from predictor.models import PsgPredictor

class PredictionForm(ModelForm):
    class Meta:
        model = PsgPredictor
        fields = ['competition', 'day', 'venue', 'opponent', 'captain', 'formation']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1','password2']