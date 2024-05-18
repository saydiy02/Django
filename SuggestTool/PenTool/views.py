from django.shortcuts import render, redirect
from .forms import SuggestToolsForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import joblib
from .models import Pentest
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
    if 'form_data' not in request.session:
        request.session['form_data'] = []

    if request.method == 'POST' and 'next' in request.POST:
        form = SuggestToolsForm(request.POST)
        if form.is_valid():
            form_data = request.session['form_data']
            form_data.append(form.cleaned_data)
            request.session['form_data'] = form_data
            return redirect('toolsSuggestion')
    elif request.method == 'POST' and 'done' in request.POST:
        form = SuggestToolsForm(request.POST)
        if form.is_valid():
            form_data = request.session['form_data']
            form_data.append(form.cleaned_data)
            request.session['form_data'] = form_data

            predictions = []
            model = joblib.load('randomfpen.pkl')
            for data in form_data:
                pentest = Pentest.objects.create(
                    goal=data['goal'],
                    typeS=data['typeS'],
                    toolsC=data['toolsC'],
                    platform=data['platform']
                )
                prediction = model.predict([[data['goal'], data['typeS'], data['toolsC'], data['platform']]])[0]
                prediction_word = "Nmap & Nikto" if prediction == 0 else "Nmap & Burpsuite"
                predictions.append({
                    'data': {
                        'goal': pentest.get_goal_display(),
                        'typeS': pentest.get_typeS_display(),
                        'toolsC': pentest.get_toolsC_display(),
                        'platform': pentest.get_platform_display()
                    },
                    'prediction': prediction_word
                })


            return render(request, 'PenTool/result.html', {'predictions': predictions})
    else:
        form = SuggestToolsForm()

    return render(request, 'PenTool/predict.html', {'form': form})