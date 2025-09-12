# bookshelf/forms.py
from django import forms


class BookSearchForm(forms.Form):
q = forms.CharField(
required=False,
max_length=200,
widget=forms.TextInput(attrs={'placeholder': 'Search by title or author'})
)


def clean_q(self):
q = self.cleaned_data.get('q', '')
# Basic sanitization: strip dangerous characters if needed
# Don't try to remove HTML here; Django templates escape by default.
return q.strip()