# Generated by Django 5.0.6 on 2024-05-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_portfolio_skill_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='percent',
            field=models.IntegerField(default=0),
        ),
    ]
