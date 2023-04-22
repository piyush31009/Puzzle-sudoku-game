from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import Score

class ScoreForm(UserCreationForm):
    
    class Meta:
        models = Score
        fields= ('user', 'time')