# Generated by Django 3.0.7 on 2020-06-06 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]