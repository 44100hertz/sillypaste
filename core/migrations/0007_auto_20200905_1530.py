# Generated by Django 3.1.1 on 2020-09-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_paste_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='body',
            field=models.TextField(unique=True),
        ),
    ]
