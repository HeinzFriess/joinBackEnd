# Generated by Django 4.2.2 on 2023-06-23 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_assigned_alter_ticket_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.category'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.priority'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.state'),
        ),
    ]