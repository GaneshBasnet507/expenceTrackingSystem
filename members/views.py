from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member#table name
from .models import User
from .models import expence
import re
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required 
from django.contrib import messages


'''def members(request):
    return HttpResponse("Hello world!")'''
def members(request):
  myuser = Member.objects.all().values()
  template = loader.get_template('master.html')
  context = {
    'myuser': myuser,
  }
  return HttpResponse(template.render(context,request))
def details(request,id):
  myuser = Member.objects.get(id=id)
  templete = loader.get_template('details.html')
  context = {
    'myuser': myuser,
  }
  return HttpResponse(templete.render(context,request))
@login_required  # Ensure only authenticated users can access this view
def addexpence(request):
    if request.method == 'POST':
        # Get the current logged-in user
        current_user = request.user

        # Create a new expense record
        Expense = expence.objects.create(
            user=current_user,  # Assign the User instance here
            particular=request.POST['particular'],
            purpose=request.POST['purpose'],
            quantity=request.POST['quantity'],
            category=request.POST['category'],
            place=request.POST['place'],
        )
        return redirect('some-view-name')  # Replace with your redirect target

    return render(request, 'addexpence.html')  # Replace with your template name
from .models import User  # Import your custom User model
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == 'POST':
        # Get the data entered by the user
        uname = request.POST['username']
        psw = request.POST['password']

        try:
            # Query the custom User table to find the user with the matching username
            user = User.objects.get(username=uname)
            print('User found:', user.username)

            # Compare the hashed password stored in the database with the entered password
            if check_password(psw, user.password):
                print('Password matched!')
                request.session['uname'] = user.username  # Storing the username in the session
                return redirect('userdashboard')  # Redirect to home page or some other page
            else:
                print('Invalid password')
                messages.error(request, 'Invalid password')
        except User.DoesNotExist:
            print('User does not exist')
            messages.error(request, 'Invalid username')

    return render(request, 'login.html')

def userdashboard(request):
        return render(request, 'userdashboard.html')
from django.contrib.auth.hashers import make_password
def register(request):
    if request.method == 'POST':
       uid = request.POST['uid']
       uname = request.POST['username']
       password = request.POST['password']
       cpass = request.POST['cpassword']
       if uname is None or len(uname)<3:
           return HttpResponse("Error, username must be more than three letter")
       if password != cpass:
            return HttpResponse("Error, password doesnot match")
       if uid is None  or int(uid) <= 0:
           return HttpResponse("Error, uid isnot valid")
       if not re.match(r'^[a-zA-Z\s]+$', uname):
           return HttpResponse("Error, username should be alphabet")
       else:
           
        new_user = User(userid=uid, username=uname, password=make_password(password))
        new_user.save()
        return HttpResponse("Registration successful, now you can login")
       ''' User =  RegisterUser(request.POST)
        if User.is_valid():
            User.save()  # Save the user data
            return redirect('login')  # Redirect to a login or another page after registration
    else:
        User = RegisterUser()  # This ensures form is defined for GET requests
'''
    return render(request, 'register.html', {'form': User})

