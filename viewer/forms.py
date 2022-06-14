from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from viewer.models import Services, Profile, ChosenServices
from django.forms import formset_factory


class ServicesForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.Textarea()


ServicesFormSet = formset_factory(ServicesForm, extra=3)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label=("Email address"), required=True,
        help_text=("Required."))
    first_name = forms.CharField(label='name', max_length=50)
    last_name = forms.CharField(label='surname', max_length=50)
    date_of_birth = forms.DateField()
    formset = ServicesFormSet()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    formset = ServicesFormSet()


class ChosenUpdateForm(forms.ModelForm):
    class Meta:
        model = ChosenServices
        exclude = []


class ServicesCreateForm(forms.ModelForm):
    class Meta:
        model = Services
        exclude = []

    name = forms.CharField(max_length=50)
    description = forms.Textarea()


class ServicesUpdateForm(forms.ModelForm):
    class Meta:
        model = Services
        exclude = []

    name = forms.CharField(max_length=50)
    description = forms.Textarea()


class ServicesSelectUpdateForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Services.objects)

