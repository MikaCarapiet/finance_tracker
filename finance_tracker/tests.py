from django.test import TestCase
from .models import User, Category, Account, Expense, Income, RecurringTransaction, Goal, Investment, Budget, Notification
from django.core.validators import MinValueValidator
# Create your tests here.


class UserAccountTests(TestCase):
    
    def user_is_created(self):
        user = User.objects.create(email="test@email.com",first_name="Test",last_name="Account",date_of_birth="2000/01/01")
        self.assertIs()