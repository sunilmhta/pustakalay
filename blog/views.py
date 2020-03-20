from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from blog.forms import RegistrationForm
from django.contrib.auth.models import User

def home(request):
	numbers=[1,2,3,4,5]
	name='Max Goodridge'

	args={'myName':name,'numbers':numbers}
	return render(request,'blog/home.html',args)


def register(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else :
		form=RegistrationForm()

	args={'form':form}
	return render(request,'blog/reg_form.html',args)

def profile(request):
	args={'user':request.user}
	return render(request,'blog/profile.html',args)

