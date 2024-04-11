# Generated by Django 4.2.4 on 2024-04-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('Requester', 'Requester'), ('Approver', 'Approver'), ('Director', 'Director')], default='Requester', max_length=9, verbose_name='Type'),
        ),
    ]
