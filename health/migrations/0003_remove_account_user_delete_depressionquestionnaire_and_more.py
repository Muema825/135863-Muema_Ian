# Generated by Django 4.2.5 on 2023-10-24 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.DeleteModel(
            name='DepressionQuestionnaire',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]