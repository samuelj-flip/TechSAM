from django.contrib import admin
from .models import Service, Lead, HunterSystem, DailyQuest  # <-- Added DailyQuest here!

# 1. Register your Services Model
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    search_fields = ('title', 'tagline')

    # 2. Register your Leads Model
    @admin.register(Lead)
    class LeadAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'project_type', 'budget', 'status', 'created_at')
        list_filter = ('status', 'created_at')
        search_fields = ('name', 'email', 'message')
        list_editable = ('status',)

        # 3. Register your Main Character Sheet Model
        @admin.register(HunterSystem)
        class HunterSystemAdmin(admin.ModelAdmin):
            list_display = ('user', 'level', 'rank', 'strength', 'agility', 'intelligence', 'sense')
            # Making stats read-only in admin so only completing quests can level them up!
            readonly_fields = ('level', 'rank')

            # 4. Register your Daily Quests Model (The Missing Piece!)
            @admin.register(DailyQuest)
            class DailyQuestAdmin(admin.ModelAdmin):
                list_display = ('task_name', 'stat_category', 'xp_reward', 'is_completed', 'date_logged')
                list_filter = ('is_completed', 'stat_category')
                list_editable = ('is_completed',)
