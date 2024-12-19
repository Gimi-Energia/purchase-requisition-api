# Generated by Django 4.2.4 on 2024-12-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_service_motive_denied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='company',
            field=models.CharField(choices=[('Gimi', 'Gimi'), ('GBL', 'GBL'), ('GPB', 'GPB'), ('GS', 'GS'), ('GIR', 'GIR'), ('Filial', 'Filial')], default='Gimi', max_length=6, verbose_name='Company'),
        ),
    ]
