# Generated by Django 5.0 on 2023-12-29 21:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0005_userapi_todo_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]