# Generated by Django 5.0.6 on 2024-09-13 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0008_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True},
        ),
    ]