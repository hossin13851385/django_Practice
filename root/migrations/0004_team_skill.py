# Generated by Django 5.0.4 on 2024-05-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_skill_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='skill',
            field=models.ManyToManyField(to='root.skill'),
        ),
    ]
