# Generated by Django 2.2 on 2021-11-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
