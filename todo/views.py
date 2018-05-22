from django.views import generic
from django.shortcuts import render, redirect
from .models import Item
from .forms import ListForm, NewTodoForm, UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User



def log_out(request):
	logout(request)
	return redirect('login')

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		user = User(username = request.POST['username'], password = request.POST['password'])
		# username = 
		user = authenticate(username = user.username, password = user.password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('index')
		else:
			print("Too bad")
			form = LoginForm()
			context = {'form' : form}
			return render(request, 'todo/login_form.html', context)


			

	else:
		form = LoginForm()
	context = {'form' : form}
	return render(request, 'todo/login_form.html', context)




class IndexView(generic.ListView):
	template_name = 'todo/index.html'
	context_object_name = 'items'

	def get_queryset(self):
		return Item.objects.all()





def index(request):
	items = Item.objects.filter(user = request.user)
	context = {'items' : items, 'current_user' : request.user}
	return render(request, 'todo/index.html', context)




def add_list(request):
	if request.method == 'POST':
		form = NewTodoForm(request.POST)

		if form.is_valid():
			list_item = form.save()
			list_item.user = request.user
			list_item.save()
			return redirect('index')

	else:
		form = NewTodoForm()
	context = {'form' : form}
	return render(request, 'todo/addlist.html', context)




def delete_entry(request, entry_id):
	entry = Item.objects.get(pk = entry_id)
	entry.delete()

	return redirect('index')

def check_completion(request, entry_id):
	entry = Item.objects.get(pk = entry_id)
	entry.check = True
	entry.save()

	return redirect('index')



class UserFormView(View):
	form_class = UserForm
	template_name = 'todo/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})

	def post(self, request):
		form = self.form_class(request.POST)


		if form.is_valid():
			user = form.save(commit = False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username = username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')

		return render(request, self.template_name, {'form' : form})

