# Generated by Django 5.1.3 on 2024-11-24 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help_enchentes', '0002_remove_report_votos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='foto',
        ),
    ]
