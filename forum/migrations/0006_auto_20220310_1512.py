# Generated by Django 3.2 on 2022-03-10 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0005_auto_20220302_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='thread',
            name='droners',
            field=models.ManyToManyField(blank=True, related_name='droners', to=settings.AUTH_USER_MODEL),
        ),
    ]