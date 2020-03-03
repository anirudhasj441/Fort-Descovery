from django.contrib import admin
from .models import Fort,Team

# Register your models here.
class FortAdmin(admin.ModelAdmin):
    search_fields = ["pk","name"]
    list_filter = ["name","date_filled"]
    list_display = [
        "pk",
        "name",
        "date_filled",
        "image",
    ]
    list_editable = ["name"]

class TeamAdmin(admin.ModelAdmin):
    search_fields = ["pk","name"]
    list_filter = ["name"]
    list_display = [
        "pk",
        "name",
        "job",
        "belogns_to",
        "email",
    ]
admin.site.register(Fort,FortAdmin)
admin.site.register(Team,TeamAdmin)
