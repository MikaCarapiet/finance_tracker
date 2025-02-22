# Generated by Django 5.1.5 on 2025-01-28 02:14

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('category_type', models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense'), ('Investment', 'Investment'), ('Account', 'Account')], max_length=15)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to='finance_tracker.category')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('account_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(limit_choices_to={'category_type': 'Account'}, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='finance_tracker.category')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(verbose_name='Date of Transaction')),
                ('description', models.TextField(blank=True, max_length=140, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='finance_tracker.account')),
                ('category', models.ForeignKey(limit_choices_to={'category_type': 'Expense'}, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='finance_tracker.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(limit_choices_to={'category_type__in': ['Income', 'Expense', 'Investment']}, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='finance_tracker.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(verbose_name='Transaction Date')),
                ('description', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='income', to='finance_tracker.account')),
                ('category', models.ForeignKey(limit_choices_to={'category_type': 'Income'}, on_delete=django.db.models.deletion.CASCADE, related_name='income', to='finance_tracker.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('current_value', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('date_invested', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(limit_choices_to={'category_type': 'Investment'}, on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='finance_tracker.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('notification_type', models.CharField(choices=[('info', 'Info'), ('warning', 'Warning'), ('alert', 'Alert')], default='info', max_length=10)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecurringTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('start_date', models.DateField()),
                ('frequency', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Biweekly', 'Biweekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=15)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(limit_choices_to={'category_type__in': ['Income', 'Expense']}, on_delete=django.db.models.deletion.CASCADE, related_name='recurring_transactions', to='finance_tracker.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recurring_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
