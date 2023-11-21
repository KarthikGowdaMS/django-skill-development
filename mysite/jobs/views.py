from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# from .models import Person, PersonForm
from jobs.models import Student
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
#from django.contrib import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView


def home(request):
    return render(request, "index.html")

# def register(request):
#     return render(request, "register.html")

# def login(request):
#     return render(request, "login.html")

# def dashboard(request):
#     return render(request, "dashboard.html")

# def person_register(request):
#     if request.method == 'POST':
#         # posted model form using person instance
#         personForm = PersonForm(request.POST)
#         # if valid form
#         #   #i save
#         #   #ii redirect to the list page
#         #   return redirect('person_list_page') 
#         if personForm.is_valid():
#             personForm.save()
#             return redirect('dashboard') 
#     else:
#         # new model form 
#         personForm = PersonForm()
        
#     return render(request, 'register.html', {'personForm':personForm}) # pass form to the page

# get current time
# from django.utils import timezone
# from datetime import datetime
# from django.utils.dateformat import DateFormat


# # write fuction to get current time
# def time(request):
#     now = datetime.now()
#     formatted_now = DateFormat(now).format('Y-m-d H:i:s')
# # render time to index2.html
#     return render(request, "index2.html", {"insert_date": formatted_now})

# def template_view(request):
#    dt=datetime.now()
#    name="Rajesh"
#    rollno=100
#    marks=90
#    dict={"name":name,"rollno":rollno,"marks":marks,"date":dt}
   
#    return render  (request,"index2.html",dict)

# Create your views here.

# def home(request):
#     return render(request, 'home.html')

@login_required(login_url = 'login')
def students(request):
    student = Student.objects.all()
    context = {'student': student}
    return render(request, 'student.html', context)

def register(request):
	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('login')


	context = { 'form': form }
	return render (request, 'register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('students')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('login')


class Forms(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'forms.html'
    success_url = '/students/'

class StudentList(ListView):
    model = Student
    template_name = 'stulist.html'

class StudentDetail(DetailView):
    model = Student
    fields = '__all__'
    template_name = 'studetail.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'stuupdate.html'
    success_url = '/students/'

class StudentDelete(DeleteView):
    model = Student
    template_name = 'studelete.html'
    success_url = '/students/'

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')







# def home(request):
# 	return render (request,"home.html", context = {})


