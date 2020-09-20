from django.urls import path
from .views import privacy_policy_view, terms_and_conditions_view

urlpatterns = [
    path('privacy_policy/', privacy_policy_view, name="privacy_policy"),
    path('terms_and_conditions/', terms_and_conditions_view, name="terms_and_conditions"),
]