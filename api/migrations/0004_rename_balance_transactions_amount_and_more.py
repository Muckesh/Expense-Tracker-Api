# Generated by Django 4.0.1 on 2022-01-27 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_transactions_isincome_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='balance',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='expense',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='income',
        ),
    ]
