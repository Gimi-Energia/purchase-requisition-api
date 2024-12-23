# Generated by Django 4.2.4 on 2024-06-26 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maintenances', '0002_remove_maintenance_approver'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_approver', to=settings.AUTH_USER_MODEL, verbose_name='Approver'),
        ),
    ]
