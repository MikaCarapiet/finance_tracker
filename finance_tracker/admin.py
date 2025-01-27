from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Account, Expense, Income, RecurringTransaction, Goal, Investment, Budget, Notification
from django.core.validators import MinValueValidator

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'user')
    list_filter = ('category_type',)
    search_fields = ('name', 'user__email')

admin.site.register(Category, CategoryAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_name", "balance", "user", "created_at", "updated_at")
    list_filter = ("user", "category")
    search_fields = ("account_name", "user__email")

admin.site.register(Account, AccountAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'account', 'date', 'user')
    list_filter = ('category', 'date')
    search_fields = ('user__email', 'category__name', 'description')

admin.site.register(Expense, ExpenseAdmin)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount','account', 'date', 'user')
    list_filter = ('category', 'date')
    search_fields = ('user__email', 'category__name', 'description')

admin.site.register(Income, IncomeAdmin)

class RecurringTransactionAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'frequency', 'start_date', 'end_date', 'user')
    list_filter = ('category', 'frequency', 'start_date')
    search_fields = ('user__email', 'category__name', 'description')

admin.site.register(RecurringTransaction, RecurringTransactionAdmin)

class GoalsAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'start_date', 'end_date', 'user')
    list_filter = ('category', 'start_date', 'end_date')
    search_fields = ('user__email', 'category__name', 'description')

admin.site.register(Goal, GoalsAdmin)

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'purchase_price', 'current_value', 'date_invested', 'user')
    list_filter = ('category', 'date_invested')
    search_fields = ('user__email', 'category__name', 'name')

admin.site.register(Investment, InvestmentAdmin)

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'start_date', 'end_date', 'user')
    list_filter = ('category', 'start_date', 'end_date')
    search_fields = ('user__email', 'category__name')

admin.site.register(Budget, BudgetAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'notification_type', 'is_read', 'created_at', 'user')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('title', 'user__email', 'message')

admin.site.register(Notification, NotificationAdmin)
