from django import forms
from .models import Pentest

class SuggestToolsForm(forms.ModelForm):
   class Meta:
      model = Pentest
      fields = '__all__'
