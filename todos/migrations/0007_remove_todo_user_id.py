# Generated by Django 5.0 on 2023-12-30 12:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0006_alter_todo_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="user_id",
        ),
    ]
