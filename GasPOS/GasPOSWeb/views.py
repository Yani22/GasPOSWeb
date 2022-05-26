from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#### ACCOUNTS ####
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, ("There Was An Error Logging In, Try Again."))
            return redirect('login')
    
    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout Success!"))
    return redirect('login')
#### ACCOUNTS ####

#### DASHBOARDS ####

def index(request):

    users = Employee.objects.filter(user=request.user, is_active=True)

    context = {
        "users":users,
    }
    return render(request, 'dashboard.html', context)

def my_account(request):
    admin = Employee.objects.get(user=request.user)
    users = Employee.objects.filter(user=request.user, is_active=True)
    form = EditEndUserForm(instance=admin)
    if request.method == 'POST':
        form = EditEndUserForm(request.POST, request.FILES, instance=admin)
        if form.is_valid():
           
            form.save()
            messages.success(request, ("Profile edit saved."))
            return redirect("my_account")
        else:
            messages.error(request, ("Profile edit failed."))
            return redirect("my_account")

    context = {
        "users":users,
        "form":form,
    }
    return render(request, 'admin_accounts/my_account.html', context)

#### DASHBOARDS  ####


#### EMPLOYEES ####
def add_employee(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user_type = request.POST['user_type']
            email = request.POST['email']
            first_name = request.POST['first_name']
            middle_name = request.POST['middle_name']
            last_name = request.POST['last_name']
            birth_date = request.POST['birth_date']
            gender_type = request.POST['gender_type']
            age = request.POST['age']
            height_cm = request.POST['height_cm']
            weight_kl = request.POST['weight_kl']
            address = request.POST['address']
            start_date =  request.POST['start_date']
            user = User.objects.create_user(username, email, password)

            if user_type == "Manager":
                employee = Employee(
                    user=user,
                    user_type=user_type,
                    email=email,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    birth_date=birth_date,
                    gender_type=gender_type,
                    age=age,
                    height_cm=height_cm,
                    weight_kl=weight_kl,
                    address=address,
                    start_date=start_date,
                    is_manager=True,
                    is_active=True
                )
                user = employee.save()

                messages.success(request, ("Employee successfully added."))
                return redirect('add_employee')

            elif user_type == "Cashier":
                employee = Employee(
                    user=user,
                    user_type=user_type,
                    email=email,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    birth_date=birth_date,
                    gender_type=gender_type,
                    age=age,
                    height_cm=height_cm,
                    weight_kl=weight_kl,
                    address=address,
                    start_date=start_date,
                    is_cashier=True,
                    is_active=True
                )
                user = employee.save()

                messages.success(request, ("Employee successfully added."))
                return redirect('add_employee')

            elif user_type == "Pumpboy":
                employee = Employee(
                    user=user,
                    user_type=user_type,
                    email=email,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    birth_date=birth_date,
                    gender_type=gender_type,
                    age=age,
                    height_cm=height_cm,
                    weight_kl=weight_kl,
                    address=address,
                    start_date=start_date,
                    is_pumpboy=True,
                    is_active=True
                )
                user = employee.save()

                messages.success(request, ("Employee successfully added."))
                return redirect('add_employee')
    else:
        form = UserCreationForm()
    context = {
        "users":users,
        "form":form,
    }
    return render(request, 'employees/add_employee.html', context)

def employee_table(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    context = {
        "users":users,
    }
    return render(request, 'employees/employee_table.html', context)

def employee_login_history(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    log_his = EmployeeLogin.objects.all()
    context = {
        "users":users,
        "log_his":log_his,
    }
    return render(request, 'employees/employee_login.html', context)

def employee_attendance(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    atte = EmployeeAttendance.objects.all()
    context = {
        "users":users,
        "atte":atte,
    }
    return render(request, 'employees/employee_attendance.html', context)
#### EMPLOYEES ####


#### GASOLINES ####

def add_gasoline(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    if request.method == "POST":
        gas_type = request.POST['gas_type']
        price_per_liter = request.POST['price_per_liter']
        date_time_added = request.POST['date_time_added']

        gas = Gasoline(
            gas_type=gas_type,
            price_per_liter=price_per_liter,
            date_time_added=date_time_added
        )
        gas.save()

    context = {
        "users":users,
    }
    return render(request, 'gasolines/add_gas.html', context)

def gas_delivery(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    gas_del = GasDelivery.objects.all()

    context = {
        "users":users,
        "gas_del":gas_del,
    }
    return render(request, 'gasolines/gas_delivery.html', context)


def gas_transaction(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    gas_trans = GasTransaction.objects.all()

    context = {
        "users":users,
        "gas_trans":gas_trans,
    }
    return render(request, 'gasolines/gas_transaction.html', context)

def manage_gasoline(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    gasoline = Gasoline.objects.all()

    context = {
        "users":users,
        "gasoline":gasoline,
    }
    return render(request, 'gasolines/manage_gas.html', context)
#### GASOLINES ####


#### ITEM #### 

def add_item(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    if request.method == "POST":
        item_name = request.POST['item_name']
        item_price = request.POST['item_price']
        no_of_items = request.POST['no_of_items']
        date_time_added = request.POST['date_time_added']

        item = Item(
            item_name=item_name,
            item_price=item_price,
            no_of_items=no_of_items,
            date_time_added=date_time_added
        )
        item.save()

    context = {
        "users":users,
    }
    return render(request, 'items/add_item.html', context)

def item_transaction(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    item_trans = ItemTransaction.objects.all()

    context = {
        "item_trans":item_trans,
        "users": users,
    }
    return render(request, 'items/item_transaction.html', context)

def manage_item(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    items = Item.objects.all()

    context = {
        "items":items,
        "users":users,
    }
    return render(request, 'items/manage_item.html', context)

#### ITEM ####


#### EXPENSES #### 

def expenses_transaction(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    expen = ExpensesTransaction.objects.all()
    context = {
        "users":users,
        "expen":expen,
    }
    return render(request, 'expenses/expenses_transaction.html', context)

def manage_expenses(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    expen = ExpensesTransaction.objects.all()
    context = {
        "users":users,
        "expen":expen,
    }
    return render(request, 'expenses/manage_expenses.html', context)

#### EXPENSES ####


#### REPORTS ####

def reports(request):
    users = Employee.objects.filter(user=request.user, is_active=True)
    daily_total = DailyTotal.objects.all()

    context = {
        "daily_total":daily_total,
        "users": users,
    }
    return render(request, 'reports/daily_totals.html', context)

#### REPORTS ####