from django import forms
from .models import Item
from django.contrib.auth.models import User

class ListForm(forms.Form):
	title = forms.CharField(max_length = 30, widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Title'}))
	description = forms.CharField(widget = forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Description'}))



class NewTodoForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['title', 'description']

		widgets = {
			'title' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Title'}),
			'description' : forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Description'}),
		}
class LoginForm(forms.ModelForm):	
	class Meta:
		
		model = User
		fields = ['username', 'password']

		widgets = {
			'username' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Username'}),
			'password' : forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Password'}),
		}

		
class UserForm(forms.ModelForm):	
	class Meta:
		
		model = User
		fields = ['username', 'email', 'password']

		widgets = {
			'username' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Username'}),
			'password' : forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Password'}),
			'email' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Email'}),
		}





