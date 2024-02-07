# Generated by Django 4.2.4 on 2024-02-07 14:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
        ('departments', '0002_remove_department_code_alter_department_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('company', models.CharField(choices=[('Gimi', 'Gimi'), ('GBL', 'GBL'), ('GPB', 'GPB'), ('GS', 'GS'), ('GIR', 'GIR')], default='Gimi', max_length=4, verbose_name='Company')),
                ('request_date', models.DateField(default=datetime.date.today, verbose_name='Request Date')),
                ('motive', models.CharField(max_length=50, verbose_name='Motive')),
                ('obs', models.TextField(verbose_name='Observation')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=8, verbose_name='Status')),
                ('approval_date', models.DateField(blank=True, null=True, verbose_name='Approval Date')),
                ('approver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Approver', to=settings.AUTH_USER_MODEL, verbose_name='Approver')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department', verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=8, verbose_name='Status')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.purchase')),
            ],
            options={
                'unique_together': {('purchase', 'product')},
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='products',
            field=models.ManyToManyField(through='purchases.PurchaseProduct', to='products.product', verbose_name='Products'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Requester', to=settings.AUTH_USER_MODEL, verbose_name='Requester'),
        ),
    ]
