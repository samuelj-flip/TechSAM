from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DailyQuest, UserStatus

@receiver(post_save, sender=DailyQuest)
def reward_quest_xp(sender, instance, created, **kwargs):
    # Only reward XP the exact moment the quest is marked as completed
    if instance.is_completed:
        # Get your profile or create it if it doesn't exist yet
        status, _ = UserStatus.objects.get_or_create(user_name="Samuel James")
        
        # Prevent double-counting if the quest is saved multiple times
        # We handle this simply by using a quick custom attribute check
        if not getattr(instance, '_xp_allocated', False):
            status.add_xp(instance.xp_reward, instance.stat_category)
            instance._xp_allocated = True