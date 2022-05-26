from django.urls import path

from . import views

urlpatterns = [
    
    #### ACCOUNTS ####
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #### ACCOUNTS ####

    #### DASHBOARDS ####
    path('dashboard/', views.index, name='dashboard'),
    path('my_account/', views.my_account, name='my_account'),
    #### DASHBOARDS ####


    #### EMPLOYEES #### 
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_table/', views.employee_table, name='employee_table'),
    path('login_history/', views.employee_login_history, name='login_history'),
    path('attendance/', views.employee_attendance, name='attendance'),
    #### EMPLOYEES ####


    #### REPORTS ####
    path('reports/', views.reports, name='reports'),
    #### REPORTS ####

    #### GASOLINE ####
    path('add_gasoline/', views.add_gasoline, name='add_gasoline'),
    path('gas_delivery/', views.gas_delivery, name='gas_delivery'),
    path('gas_transaction/', views.gas_transaction, name='gas_transaction'),
    path('manage_gasoline/', views.manage_gasoline, name='manage_gasoline'),
    #### GASOLINE ####    

    #### ITEM ####
    path('add_item/', views.add_item, name='add_item'),
    path('item_transaction/', views.item_transaction, name='item_transaction'),
    path('manage_item/', views.manage_item, name='manage_item'),
    #### ITEM ####

    #### EXPENSES ####
    path('expenses_transaction/', views.expenses_transaction, name='expenses_transaction'),
    path('manage_expenses/', views.manage_expenses, name='manage_expenses'),
    #### EXPENSES ####


]