''''
implements view of main app



'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SkillForm
from .models import Skill
from django.contrib.auth.models import User

def homepage(request):
    """
    Render the homepage template.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered homepage HTML.
    """
    return render(request, 'main/homepage.html')


def add_skill(request):
    """
    Handle form submission for adding a new skill, or display the form.

    If the request method is POST, it validates and saves the skill form.
    Otherwise, it renders an empty form.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered add skill page with a form and list of skills.
    """
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills_list')  # Redirect to the skills list
    else:
        form = SkillForm()
    
    return render(request, 'main/add_skill.html', {'form': form})


def skills_list(request):
    """
    View to list all skills stored in the database.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered skills list page with all skills passed in the context.
    """
    skills = Skill.objects.all()  # Fetch all skills from the database
    return render(request, 'main/skills_list.html', {'skills': skills})


def contact(request):
    """
    Render the contact page template.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered contact page HTML.
    """
    return render(request, 'main/contact.html')


def news(request):
    """
    Render the news page template.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered news page HTML.
    """
    return render(request, 'main/news.html')


def register(request):
    """
    Handle user registration by collecting username, password, and email.

    If a POST request is received, it checks if the username already exists
    and creates a new user if it does not. Otherwise, it renders the registration form.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered registration page or redirect to login upon success.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Debug statement to see the username being checked
        print(f"Trying to register username: {username}")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'main/register.html')

        User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')
    
    return render(request, 'main/register.html')


def login_view(request):
    """
    Handle custom user login by authenticating the username and password.

    If a POST request is made, it authenticates the user using the provided credentials.
    Upon successful authentication, it redirects to the homepage.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered login page or redirect to homepage on success.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'main/login.html')


def user_login(request):
    """
    Handle user login using Django's built-in AuthenticationForm.

    On POST requests, it authenticates the user via the AuthenticationForm. 
    On GET requests, it renders the empty login form.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered login page with the form or redirect on successful login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html', {'form': form})
