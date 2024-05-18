from django.urls import path
from .views import toolsSuggestion
from . import views

urlpatterns = [
   path('', toolsSuggestion, name='toolsSuggestion'),

]
