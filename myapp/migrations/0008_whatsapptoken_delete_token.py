# Generated by Django 4.2.5 on 2023-12-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsAppToken',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'token',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]
