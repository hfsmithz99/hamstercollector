# Generated by Django 5.0 on 2023-12-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_alter_feeding_options_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamster',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
