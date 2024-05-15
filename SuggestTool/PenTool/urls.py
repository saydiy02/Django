from django.urls import path
from .views import toolsSuggestion

urlpatterns = [
   path('', toolsSuggestion, name='toolsSuggestion'),
]
