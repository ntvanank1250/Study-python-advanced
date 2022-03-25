from django import forms


class EmailForm(forms.Form):
    subject = "Hello"
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)