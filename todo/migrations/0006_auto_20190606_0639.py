# Generated by Django 2.2.1 on 2019-06-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20190604_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='deaddate',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='deadtime',
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
