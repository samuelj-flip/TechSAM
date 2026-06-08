from django.contrib import admin
from .models import Service, Lead, HunterSystem

# 1. Register your Services Model
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    search_fields = ('title', 'tagline')

# 2. Register your Leads Model (This makes the 'Leads' row appear!)
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_type', 'budget', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_editable = ('status',)

from django.contrib import admin
from .models import HunterSystem

@admin.register(HunterSystem)
class HunterSystemAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'rank', 'strength', 'agility', 'intelligence', 'sense')