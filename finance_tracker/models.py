from django.db import models
from django.core.validators import MinValueValidator
from users.models import User
class Category(models.Model):
    # Decided to go with one category model for consistency in models
    class Meta:
        unique_together = ("user", "name")

    ACCOUNT = "Account"
    INCOME = "Income"
    EXPENSE = "Expense"
    INVESTMENT = "Investment"

    CATEGORY_TYPE_CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
        (INVESTMENT, "Investment"),
        (ACCOUNT, "Account"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="categories",null=True,blank=True,)
    name = models.CharField(max_length=50,unique=True)
    category_type = models.CharField(max_length=15,choices=CATEGORY_TYPE_CHOICES)
    
    def __str__(self):
        # Display the category name and type (optional)
        return f"{self.name} ({self.category_type})"

class Account(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="accounts")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="accounts",limit_choices_to={"category_type":"Account"},)
    balance = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)]) 
    account_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_name} - ({self.balance})"
    
    def add_income(self, amount): # Method that adds any Income to balance of the account

        self.balance += amount
        self.save() 

    def deduct_expense(self, amount): # Method that adds any Expense to balance of the account
        self.balance -= amount
        if self.balance < 0:
            raise ValueError("Balance cannot be negative.")  
        self.save()
    
    def get_balance(self): # Method that gets balance of the account

        return self.balance
    

class Expense(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="expenses")
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="expenses",null=True,blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10,validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="expenses",limit_choices_to={"category_type":"Expense"},)
    date = models.DateField("Date of Transaction")
    description = models.TextField(max_length=140,null=True,blank=True)

    def save(self, *args, **kwargs):
        # Check if this is a new expense
        is_new = self.pk is None
        if is_new:
            self.account.deduct_expense(self.amount)  # Update account balance
        else:
            # Handle updates to existing expense (optional, e.g., adjust balance if amount changes)
            old_expense = Expense.objects.get(pk=self.pk)
            if old_expense.amount != self.amount:
                self.account.balance += old_expense.amount  # Reverse old amount
                self.account.balance -= self.amount         # Deduct new amount
                self.account.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Add back the expense amount to the account balance when deleted
        self.account.balance += self.amount
        self.account.save()
        super().delete(*args, **kwargs)


    def __str__(self):
        return f"{self.category.name} - ({self.amount})"


class Income(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="income")
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="income",null=True,blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10,validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="income",limit_choices_to={"category_type":"Income"},)
    date = models.DateField("Transaction Date")
    description = models.TextField(blank=True,null=True)
   
    def save(self, *args, **kwargs):
        # Check if this is a new income
        is_new = self.pk is None
        if is_new:
            self.account.add_income(self.amount)  # Update account balance
        else:
            # Handle updates to existing income (optional, e.g., adjust balance if amount changes)
            old_income = Income.objects.get(pk=self.pk)
            if old_income.amount != self.amount:
                self.account.balance -= old_income.amount  # Reverse old amount
                self.account.balance += self.amount       # Add new amount
                self.account.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Deduct the income amount from the account balance when deleted
        self.account.balance -= self.amount
        self.account.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} - ({self.amount})"


class RecurringTransaction(models.Model):
# Define transaction type choices
 
    # Define frequency choices
    DAILY = "Daily"
    WEEKLY = "Weekly"
    BIWEEKLY = "Biweekly"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"
    FREQUENCY_CHOICES = [
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
        (BIWEEKLY, "Biweekly"),
        (MONTHLY, "Monthly"),
        (YEARLY, "Yearly"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recurring_transactions")
    amount = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="recurring_transactions",limit_choices_to={"category_type__in":
    ["Income","Expense"]},)
    start_date = models.DateField()  # When the recurring transaction begins
    frequency = models.CharField(max_length=15,choices=FREQUENCY_CHOICES)
    end_date = models.DateField(null=True, blank=True)  # When it ends (optional)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.category.name} - ({self.amount})"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goal")
    amount = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="goals",limit_choices_to={"category_type__in":
    ["Income","Expense","Investment"]},)    
    start_date = models.DateField()  # When the goal begins
    end_date = models.DateField(null=True, blank=True)  # When it ends (optional)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.category.name} Goal: ${self.amount}"


class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="investments")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="investments",limit_choices_to={"category_type":"Investment"},)
    name = models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2,validators=[MinValueValidator(0)])
    current_value = models.DecimalField(max_digits=15, decimal_places=2,null=True,blank=True)
    date_invested = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - ${self.current_value or 'N/A'}"
    
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="budgets"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Budget limit
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.category.name} Budget: {self.amount} ({self.start_date} to {self.end_date})"

    def is_exceeded(self):
        # Calculate total expenses in the budgeted category
        total_expenses = Expense.objects.filter(
            user=self.user,
            category=self.category,
            date__range=(self.start_date, self.end_date),
        ).aggregate(total=models.Sum("amount"))["total"]
        total_expenses = total_expenses or 0
        return total_expenses > self.amount
    
class Notification(models.Model):
    INFO = "info"
    WARNING = "warning"
    ALERT = "alert"

    NOTIFICATION_TYPE_CHOICES = [
        (INFO, "Info"),
        (WARNING, "Warning"),
        (ALERT, "Alert"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPE_CHOICES, default=INFO)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title[:30]} ({self.notification_type})"
    

