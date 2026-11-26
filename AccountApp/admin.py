from django.contrib import admin

from .models import Doctor, Patient, Specialty, User

admin.site.register(User)
admin.site.register(Specialty)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'license_number', 'phone')
    filter_horizontal = ('specialties',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # modification -> identifiant métier figé
            return ('license_number',)
        return ()


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'national_id', 'phone', 'birth_date')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('national_id',)
        return ()
