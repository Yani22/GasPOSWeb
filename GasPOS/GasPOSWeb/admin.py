from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeLogin)
admin.site.register(EmployeeAttendance)
admin.site.register(Gasoline)
admin.site.register(GasDelivery)
admin.site.register(GasTransaction)
admin.site.register(Item)
admin.site.register(ItemTransaction)
admin.site.register(ExpensesTransaction)
admin.site.register(DailyTotal)
