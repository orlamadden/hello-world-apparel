from django.shortcuts import render


def privacy_policy_view(request, *args, **kwargs):
    """
    Renders view for the privacy policy page
    """
    return render(request, "privacy_policy.html")


def terms_and_conditions_view(request, *args, **kwargs):
    """
    Renders view for the privacy policy page
    """
    return render(request, "terms_and_conditions.html")