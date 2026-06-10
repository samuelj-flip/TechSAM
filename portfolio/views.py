from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Service, Lead, HunterSystem

def home(request):
    # 1. CATCH INCOMING DATA (When user submits the form)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        project_type = request.POST.get("project_type")
        budget = request.POST.get("budget")
        message = request.POST.get("message")

        # Save it straight into your PostgreSQL database
        Lead.objects.create(
        name=name,
        email=email,
        project_type=project_type,
        budget=budget,
        message=message,
        )

        # Queue up the success banner
        messages.success(
        request,
        "Your message has been logged! I will review your project parameters shortly.",
        )
        return redirect("home")

    # 2. DISPLAY DATA (Normal page viewing)
    services = Service.objects.filter(is_active=True)
    context = {"services": services}
    return render(request, "portfolio/index.html", context)


@login_required
def system_dashboard(request):
    # Security Lockdown: Only allow the absolute site owner/superuser
    if not request.user.is_superuser:
        raise Http404("Page not found")

    # Fetch or auto-create the hunter profile for you
    hunter_stats, created = HunterSystem.objects.get_or_create(user=request.user)

    context = {"system": hunter_stats}
    return render(request, "portfolio/system_dashboard.html", context)

@login_required(login_url="/admin/login/")
def hunter_status_view(request):
    if not request.user.is_superuser:
        raise Http404("Page not found")

    try:
        hunter = HunterSystem.objects.get(user=request.user)
    except HunterSystem.DoesNotExist:
        hunter = HunterSystem.objects.first()

    if not hunter:
        hunter = HunterSystem.objects.create(
            user=request.user,
            level=1,
            rank="E-Rank",
            strength=10,
            agility=10,
            intelligence=10,
            sense=10
        )

    # Everything below this line is perfectly aligned to execute every single time!
    next_level_xp = hunter.level * 100
    current_xp = getattr(hunter, 'xp', getattr(hunter, 'total_xp', 0))
    xp_percentage = (current_xp / next_level_xp) * 100 if next_level_xp > 0 else 0

    context = {
        "hunter": hunter,
        "current_xp": current_xp,
        "xp_percentage": xp_percentage,
        "next_level_xp": next_level_xp,
    }
    
    return render(request, "portfolio/hunter_status.html", context)
