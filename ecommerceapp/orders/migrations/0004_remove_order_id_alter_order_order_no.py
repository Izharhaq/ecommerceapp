# Generated by Django 4.2.13 on 2024-06-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_created_by_order_order_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.CharField(default=0, editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
