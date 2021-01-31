from django.contrib import admin

# Register your models here.
from .models import Income,Expense

class incomeAdmin(admin.ModelAdmin):
    list_display=['income','income_date','income_type','description','user']
    list_filter=['income','income_date']  # you can filter based on gender etc

class expenseAdmin(admin.ModelAdmin):
    list_display=['expense','expense_date','expense_type','description','user']
    
    
admin.site.register(Income, incomeAdmin)
admin.site.register(Expense, expenseAdmin)
