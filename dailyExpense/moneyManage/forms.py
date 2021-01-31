from .models import userRegister, User, Income, Expense
from django import forms
from django.contrib.auth.forms import UserCreationForm

class user_form(UserCreationForm):
    class Meta:
        model = userRegister
        fields = ('first_name','username','email','age','contact')

class Income_form(forms.ModelForm):
    income = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'enter income '}))
    income_type = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter income type'}) )
    description = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter description'}) )
    class Meta:
        model = Income
        fields = '__all__'

class Expense_form(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class Login_form(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget =forms.PasswordInput) 