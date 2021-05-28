from django.contrib import admin
from .models import Staff, Patient, AppointmentSchedule, Doctor, Vaccine, Vaccination, Payment, VaccineStock, CustomUser

# admin.site.register(CustomUser)

# Register your models here.
@admin .register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'email_id', 'age', 'address')

@admin .register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'appointment_number')
    list_filter = ('patient_name',)

@admin .register(AppointmentSchedule)
class AppointmentScheduleAdmin(admin.ModelAdmin):
    list_display = ('appointment_number', 'time', 'date')

@admin .register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'appointment_number', 'time', 'date', 'bill')

@admin .register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'paid_amount', 'due_amount')

@admin .register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ('vaccine_name', 'price', 'stock_quantity')

@admin .register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    list_display = ('appointment_number', 'vaccine_name')

@admin .register(VaccineStock)
class VaccineStockAdmin(admin.ModelAdmin):
    list_display = ('stock_in', 'stock_out', 'current_stock')

@admin .register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "profile_image")