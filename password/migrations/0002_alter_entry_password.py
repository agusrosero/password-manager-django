# Generated by Django 5.0.2 on 2024-02-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
