# Generated by Django 5.1.2 on 2025-04-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_rename_owner_pet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='is_sleeping',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='sleep_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
