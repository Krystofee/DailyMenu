# Generated by Django 2.0 on 2018-01-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuentry',
            name='price',
            field=models.CharField(max_length=150, verbose_name='Price'),
        ),
    ]
