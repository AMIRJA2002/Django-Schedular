# Generated by Django 4.0.7 on 2024-01-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='precondition_tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='precondition_tasks',
            field=models.ManyToManyField(blank=True, related_name='pre_tasks', to='schedule.task'),
        ),
    ]
