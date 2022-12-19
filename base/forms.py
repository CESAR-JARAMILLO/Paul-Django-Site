from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Subject', 'style': 'width: 300px;', 'class': 'form-control'}))