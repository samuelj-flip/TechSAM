from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, Lead
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import HunterSystem

def home(request):
    # 1. CATCH INCOMING DATA (When user submits the form)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        project_type = request.POST.get('project_type')
        budget = request.POST.get('budget')
        message = request.POST.get('message')
        
        # Save it straight into your PostgreSQL database
        Lead.objects.create(
            name=name,
            email=email,
            project_type=project_type,
            budget=budget,
            message=message
        )
        
        # Queue up the success banner
        messages.success(request, "Your message has been logged! I will review your project parameters shortly.")
        return redirect('home')

    # 2. DISPLAY DATA (Normal page viewing)
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services
    }
    return render(request, 'portfolio/index.html', context)

@login_required
def system_dashboard(request):
    # Security Lockdown: Only allow the absolute site owner/superuser
    if not request.user.is_superuser:
        raise Http404("Page not found")
        
    # Fetch or auto-create the hunter profile for you
    hunter_stats, created = HunterSystem.objects.get_or_create(user=request.user)
    
    context = {
        'system': hunter_stats
    }
    return render(request, 'portfolio/system_dashboard.html', context)