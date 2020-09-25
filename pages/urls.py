from django.urls import path
from .views import privacy_policy_view, terms_and_conditions_view, about_us_view, faq_view

urlpatterns = [
    path('privacy_policy/', privacy_policy_view, name="privacy_policy"),
    path('terms_and_conditions/', terms_and_conditions_view, name="terms_and_conditions"),
    path('about_us/', about_us_view, name="about_us"),
    path('faq/', faq_view, name="faq"),
]