# Generated by Django 4.2.5 on 2023-09-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='descr',
            field=models.CharField(default="", max_length=500),
            preserve_default=False,
        ),
    ]
