# Generated by Django 5.0.3 on 2024-03-20 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_comments"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.CharField(max_length=100)),
                ("created", models.DateTimeField(auto_now=True)),
                ("posted_by", models.CharField(max_length=100)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="posts.post",
                    ),
                ),
            ],
            options={
                "ordering": ("created",),
            },
        ),
        migrations.DeleteModel(
            name="comments",
        ),
    ]