from django.contrib import admin
from . import models
from .models import Card

admin.site.register(Card)

class SubjectsInLine(admin.TabularInline):
    model = models.Subject
    extra = 0
    
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "sets", "_subjects")
    search_field = ["user__username"]
    
    inlines = [SubjectsInLine]
    
    def _subjects(self, obj):
        return obj.subjects.all().count()
        