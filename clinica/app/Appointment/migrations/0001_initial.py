# Generated by Django 5.1.1 on 2024-09-27 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('Programada', 'Programada'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')], max_length=50)),
                ('doctor', models.ForeignKey(limit_choices_to={'role': 'Médico'}, on_delete=django.db.models.deletion.CASCADE, to='User.user')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.patient')),
            ],
        ),
    ]
