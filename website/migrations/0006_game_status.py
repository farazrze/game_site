# Generated by Django 5.0.4 on 2024-04-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_category_game_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
