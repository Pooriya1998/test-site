from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    subject = forms.CharField(max_length=255,  required=False)


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    name = forms.CharField(max_length=255)

    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
