# Generated by Django 5.1.2 on 2024-10-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
