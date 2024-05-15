from django.shortcuts import render
from .forms import SuggestToolsForm
import joblib
# Create your views here.
def home (request):
    return render(request, 'PenTool/home.html')

def toolsSuggestion(request):
    if request.method == 'POST':
        form = SuggestToolsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("Form data:", data)  # Debug print
            model = joblib.load('randomfpen.pkl')
            print("Model loaded successfully")  # Debug print
            prediction = model.predict([list(data.values())])
            print("Prediction:", prediction)  # Debug print
            return render(request, 'PenTool/result.html', {'prediction': prediction})
        else:
            print("Form is not valid:", form.errors)  # Debug print
    else:
        form = SuggestToolsForm()
    
    return render(request, 'PenTool/predict.html', {'form': form})
