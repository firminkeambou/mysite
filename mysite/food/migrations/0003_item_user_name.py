# Generated by Django 4.2 on 2024-08-01 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user_name',
            field=models.ForeignKey(default=18, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
