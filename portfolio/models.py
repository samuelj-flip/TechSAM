from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    ICON_CHOICES = [
        ('code', 'Web Development / Next.js / Django'),
        ('terminal', 'Automation & Scraping / Playwright'),
        ('cpu', 'AI Integration & Logic Trees'),
    ]

    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255, help_text="A high-impact business value one-liner.")
    description = models.TextField(help_text="Detailed description of deliverables.")
    icon_type = models.CharField(max_length=20, choices=ICON_CHOICES, default='code')
    is_active = models.BooleanField(default=True, help_text="Toggle visibility on homepage.")
    display_order = models.IntegerField(default=0, help_text="Controls sorting order.")

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title
    
class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New / Unread'),
        ('contacted', 'Contacted / In Progress'),
        ('closed', 'Closed / Won'),
        ('archived', 'Archived / Spam'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    # REMOVED placeholder here:
    project_type = models.CharField(max_length=100) 
    budget = models.CharField(max_length=50, blank=True, null=True, help_text="Estimated budget range")
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.project_type}"

class HunterSystem(models.Model):
    RANK_CHOICES = [
        ('E', 'E-Rank Intern'),
        ('D', 'D-Rank Junior'),
        ('C', 'C-Rank Developer'),
        ('B', 'B-Rank Full-Stack'),
        ('A', 'A-Rank Elite Engineer'),
        ('S', 'S-Rank Monarch'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hunter_profile')
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=1, choices=RANK_CHOICES, default='E')
    
    # Attributes (Tech Stack Stats)
    strength = models.IntegerField(default=10, help_text="Backend (Django, PostgreSQL, SQL)")
    agility = models.IntegerField(default=10, help_text="Frontend (React, Next.js, Tailwind)")
    intelligence = models.IntegerField(default=10, help_text="AI/ML & Core Python")
    sense = models.IntegerField(default=10, help_text="Debugging & System Architecture")
    
    # Daily Quest Tracking
    quest_code_committed = models.BooleanField(default=False)
    quest_docs_read = models.BooleanField(default=False)
    quest_logic_solved = models.BooleanField(default=False)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Level {self.level} [{self.get_rank_display()}]"
