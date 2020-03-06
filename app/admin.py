from django.contrib import admin
from .models import Fort,Team,ContactForm,Profile
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

class ContactFormAdmin(admin.ModelAdmin):
    search_fields = ["pk","name","message"]
    list_filter = ["name","created_at"]
    list_display = [
        "pk",
        "name",
        "email",
        "created_at",
        "message"
    ]

class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "name",
        "contact",
        "email",
    ]

admin.site.register(Fort,FortAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(ContactForm,ContactFormAdmin)
admin.site.register(Profile,ProfileAdmin)