# Generated by Django 4.1.6 on 2023-02-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapp',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='myapp',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
