from django.contrib import admin

# Register your models here.

from .models import AccountInfo
admin.site.register(AccountInfo)

from .models import BudgetInfo
admin.site.register(BudgetInfo)



