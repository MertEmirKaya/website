# Generated by Django 4.0.5 on 2022-07-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
