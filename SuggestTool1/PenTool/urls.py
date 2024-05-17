from django.urls import path
from .views import toolsSuggestion
from . import views

urlpatterns = [
   path('', toolsSuggestion, name='toolsSuggestion'),
    #path('login/', views.login_view, name='login'),
    #path('register/', views.register_view, name='register'),
]
