# Generated by Django 2.2.1 on 2019-05-08 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_board_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='body',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]