from django import forms

from .models import Bet

class BetForm(forms.ModelForm):

    class Meta:
        model = Bet
        fields = ('team1', 'team2', 'score1', 'score2', 'date', 'ratio', 'rate', 'description')