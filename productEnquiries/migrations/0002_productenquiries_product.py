# Generated by Django 3.1 on 2020-09-07 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200905_0623'),
        ('productEnquiries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productenquiries',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productenquiries', to='products.product'),
        ),
    ]