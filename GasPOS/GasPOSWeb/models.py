from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    user_type = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    gender_type = models.CharField(max_length=255, null=True)
    age = models.IntegerField(blank=True)
    height_cm = models.IntegerField(blank=True)
    weight_kl = models.IntegerField(blank=True)
    address = models.CharField(max_length=255, null=True)
    birth_date = models.CharField(max_length=255, null=True)
    start_date = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(upload_to='images/', null=True,blank=True)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)
    is_pumpboy = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

class EmployeeLogin(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    date_logged_in = models.CharField(max_length=255, null=True)
    date_logged_out = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.date_logged_in

class EmployeeAttendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    datetime_logged_in = models.CharField(max_length=255, null=True)
    datetime_logged_out = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.datetime_logged_out

class Gasoline(models.Model):
    gas_type = models.CharField(max_length=255, null=True)
    price_per_liter = models.IntegerField(blank=True)
    date_time_added = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.gas_type

class GasDelivery(models.Model):
    gasoline = models.ForeignKey(Gasoline, on_delete=models.CASCADE, blank=True, null=True)
    kl = models.IntegerField(blank=True)
    date_time_delivered = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.date_time_delivered

class GasTransaction(models.Model):
    gasoline = models.ForeignKey(Gasoline, on_delete=models.CASCADE, blank=True, null=True)
    in_charge = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    liter_quantity = models.IntegerField(blank=True)
    liter_price = models.IntegerField(blank=True)
    total_amount = models.IntegerField(blank=True)
    date_time_purchased = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.date_time_purchased

class Item(models.Model):
    item_name = models.CharField(max_length=255, null=True)
    item_price = models.IntegerField(blank=True)
    no_of_items = models.IntegerField(blank=True)
    date_time_added = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.item_name

class ItemTransaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    in_charge = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    item_quantity = models.IntegerField(blank=True)
    total_amount = models.IntegerField(blank=True)
    date_time_purchased = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.date_time_purchased

class ExpensesTransaction(models.Model):
    name = models.CharField(max_length=255, null=True)
    in_charge = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    item = models.CharField(max_length=255, null=True)
    total_amount = models.IntegerField(blank=True)
    date_time_expensed = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class DailyTotal(models.Model):
    in_charge = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    total_recorded_sales = models.IntegerField(blank=True)
    total_amount_liters_discount = models.IntegerField(blank=True)
    total_amount_of_deficit = models.IntegerField(blank=True)
    total_amount_of_excess = models.IntegerField(blank=True)
    total_amount_deposited = models.IntegerField(blank=True)
    total_expenses = models.IntegerField(blank=True)
    date_time_reported = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.date_time_reported