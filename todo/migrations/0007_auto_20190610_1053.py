# Generated by Django 2.2.1 on 2019-06-10 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0006_auto_20190606_0639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='users',
        ),
        migrations.AddField(
            model_name='todo',
            name='users',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
