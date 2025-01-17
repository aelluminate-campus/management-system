# Generated by Django 5.1.1 on 2024-10-03 07:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_of_products',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Food', 'Food')], max_length=50, null=True),
        ),
    ]
