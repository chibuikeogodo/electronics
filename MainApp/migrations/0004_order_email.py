# Generated by Django 3.1.13 on 2023-08-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20230814_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=None, max_length=300),
        ),
    ]