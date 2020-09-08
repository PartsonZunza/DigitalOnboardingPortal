from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class OrderForm(ModelForm):
    class Meta:
        fields = '__all__'


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class CreatingMyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()

class OnBoardingPortal:

    new_product=0
    new_product_name=''