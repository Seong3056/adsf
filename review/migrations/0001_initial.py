# Generated by Django 5.0.1 on 2024-02-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100, verbose_name="포스트 제목")),
                ("content", models.TextField(verbose_name="포스트 내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일시"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="글수정시간"),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True, upload_to="post", verbose_name="썸네일 이미지"
                    ),
                ),
            ],
        ),
    ]
