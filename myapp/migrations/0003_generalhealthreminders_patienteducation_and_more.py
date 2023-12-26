# Generated by Django 4.2.5 on 2023-11-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_attachmentreminder_recurrence'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralHealthReminders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=20)),
            ],
            options={
                'db_table': 'general_health_reminders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientEducation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=20)),
            ],
            options={
                'db_table': 'patient_education',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProcedureInstruction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=20)),
            ],
            options={
                'db_table': 'procedure_instruction',
                'managed': False,
            },
        ),
    ]
