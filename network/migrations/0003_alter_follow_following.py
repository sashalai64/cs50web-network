# Generated by Django 4.2.1 on 2024-07-30 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0002_post_like_follow"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="following",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followed",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
