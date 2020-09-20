from django.shortcuts import render

def about_us_view(request, *args, **kwargs):
    """
    Renders view for the about us page
    """
    return render(request, "about_us.html")


def privacy_policy_view(request, *args, **kwargs):
    """
    Renders view for the privacy policy page
    """
    return render(request, "privacy_policy.html")


def terms_and_conditions_view(request, *args, **kwargs):
    """
    Renders view for the terms and conditions page
    """
    return render(request, "terms_and_conditions.html")