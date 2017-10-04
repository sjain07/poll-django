"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from app.models import Choice, Poll, Patient, Doctor, Prescription

class ChoiceInline(admin.TabularInline):
    """Choice objects can be edited inline in the Poll editor."""
    model = Choice
    extra = 3

class PrescriptionInline(admin.TabularInline):
    """Choice objects can be edited inline in the Poll editor."""
    model = Prescription

class PollAdmin(admin.ModelAdmin):
    """Definition of the Poll editor."""
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['text']
    date_hierarchy = 'pub_date'

class DoctorAdmin(admin.ModelAdmin):
    inlines = [PrescriptionInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Patient)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Prescription)
