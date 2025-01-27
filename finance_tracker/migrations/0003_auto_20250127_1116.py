from django.db import migrations

def populate_categories(apps, schema_editor):
    Category = apps.get_model("finance_tracker", "Category")

    predefined_categories = [
        # Income categories
        {"name": "Salary", "category_type": "Income"},
        {"name": "Bonus", "category_type": "Income"},
        {"name": "Investment Returns", "category_type": "Income"},

        # Expense categories
        {"name": "Rent", "category_type": "Expense"},
        {"name": "Utilities", "category_type": "Expense"},
        {"name": "Groceries", "category_type": "Expense"},
        {"name": "Food", "category_type": "Expense"},
        {"name": "Entertainment", "category_type": "Expense"},

        # Investment categories
        {"name": "Stocks", "category_type": "Investment"},
        {"name": "Cryptocurrency", "category_type": "Investment"},
        {"name": "Real Estate", "category_type": "Investment"},

        # Account categories
        {"name": "Checking Account", "category_type": "Account"},
        {"name": "Savings Account", "category_type": "Account"},
        {"name": "Credit Card", "category_type": "Account"},
    ]

    for category_data in predefined_categories:
        Category.objects.get_or_create(**category_data)

def remove_categories(apps, schema_editor):
    Category = apps.get_model("finance_tracker", "Category")

    predefined_category_names = [
        "Salary", "Freelancing", "Investment Returns",
        "Rent", "Utilities", "Groceries", "Entertainment",
        "Stocks", "Cryptocurrency", "Real Estate",
        "Checking Account", "Savings Account", "Credit Card",
    ]

    Category.objects.filter(name__in=predefined_category_names).delete()

class Migration(migrations.Migration):
    dependencies = [
        ("finance_tracker", "0001_initial"),  # Ensure this runs after the initial migration
    ]

    operations = [
        migrations.RunPython(populate_categories, remove_categories),
    ]
