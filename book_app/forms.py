from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=12)
    surname = forms.CharField(min_length=3, max_length=12)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 5}))
    rating = forms.IntegerField(min_value=1, max_value=5)