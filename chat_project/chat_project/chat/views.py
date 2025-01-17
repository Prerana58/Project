from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensure the user is logged in to access this page
def chat_home(request):
    return render(request, 'chat/chat_home.html')

# Sign-up view
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat/sign_up.html', {'form': form})

# Login view
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat_home')
    return render(request, 'chat/login.html')



from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from django.contrib.auth.models import User

@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/chat_home.html', {'users': users})

@login_required
def chat_with_user(request, user_id):
    user = User.objects.get(id=user_id)
    chat, created = Chat.objects.get_or_create(user1=request.user, user2=user)

    # Retrieve old messages
    messages = Message.objects.filter(chat=chat).order_by('created_at')

    return render(request, 'chat/chat_room.html', {
        'chat': chat,
        'messages': messages,
        'user': user
    })


from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat_home')  # Redirect after login
    else:
        form = AuthenticationForm()

    return render(request, 'chat/login.html', {'form': form})

# chat/views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def log_out(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logging out

