from django import forms

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    files = forms.FileField()

class Animal (forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    color = forms.CharField(max_length=20)
    