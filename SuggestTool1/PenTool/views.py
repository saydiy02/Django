from django.shortcuts import render, redirect
from .forms import SuggestToolsForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import joblib
# Create your views here.
def home (request):
    return render(request, 'PenTool/home.html')

def login_view(request):
    login_error = False  # Initialize login error flag
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to toolsSuggestion or another page
            return redirect('toolsSuggestion')
        else:
            # Set login_error to True if authentication fails
            login_error = True

    return render(request, 'PenTool/login.html', {'login_error': login_error})


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        # Optionally, you can log the user in automatically after registration
        login(request, user)
        # Redirect to dashboard or another page
        return redirect('toolsSuggestion')
    return render(request, 'PenTool/register.html')


def toolsSuggestion(request):
    if request.method == 'POST':
        form = SuggestToolsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("Form data:", data)  # Debug print
            model = joblib.load('randomfpen.pkl')
            print("Model loaded successfully")  # Debug print
            prediction = model.predict([list(data.values())])
            prediction_word = "Nmap & Nikto" if prediction == 0 else "Nmap & Burpsuite"
            print("Prediction:", prediction)  # Debug print
            return render(request, 'PenTool/result.html', {'prediction': prediction})
        else:
            print("Form is not valid:", form.errors)  # Debug print
    else:
        form = SuggestToolsForm()
    
    return render(request, 'PenTool/predict.html', {'form': form})
