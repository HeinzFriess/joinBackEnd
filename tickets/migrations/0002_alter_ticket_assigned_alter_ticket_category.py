# Generated by Django 4.2.2 on 2023-06-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]