from django import forms

from .models import BoardItem


class BoardForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea'})
    )

    written_by_name = forms.CharField(
        max_length=100, required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    written_by_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'input'})
    )

    private = forms.BooleanField(required=False)
