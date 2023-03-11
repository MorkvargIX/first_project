from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 5}))