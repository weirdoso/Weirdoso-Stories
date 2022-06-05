from django import forms
from .models import BookPost, Comment, Subscribers


class BookPostForm(forms.ModelForm):
    class Meta:
        model = BookPost
        fields = ('title', 'author', 'body', 'header_image', 'wattpad_link')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'show', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What is the book all about?'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'wattpad_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Wattpad Link'})
        }

    def __init__(self, *args, **kwargs):
        super(BookPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ""
        self.fields['body'].label = ""
        self.fields['header_image'].label = ""
        self.fields['wattpad_link'].label = ""


class SubscribersForm (forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('emailaddress',)

        widgets = {
            'emailaddress': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Email Address'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscribersForm, self).__init__(*args, **kwargs)
        self.fields['emailaddress'].label = ""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What can you say about the book?'}),
              }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['body'].label = ""


class EditBookForm(forms.ModelForm):
     class Meta:
        model = BookPost
        fields = ('title', 'body', 'header_image', 'wattpad_link')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'wattpad_link': forms.TextInput(attrs={'class': 'form-control'})
        }

