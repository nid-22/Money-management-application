from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('Add_Income', v.add_income, name='Add_Income'),
    path('Add_Expense',v.add_expense, name='Add_Expense'),
    path('Income_list',v.income_list, name='Income_list'),
    path('Expense_list', v.expense_list, name='Expense_list'),
    path('register', v.register, name='register'),
    path('login', v.login, name='login'),
    path('logout', v.logout, name='logout'),
    path('home', v.homepage, name='home'),
     path('delete_income/<int:id>/',v.delete_income,name='d_income'),
    path('delete_expense/<int:id>/',v.delete_expense,name='d_expense'),
    path('update_expense/<int:id>/',v.update_income,name='d_update'),
    path('edit_profile',v.edit_profile,name='edf'),
    
]
