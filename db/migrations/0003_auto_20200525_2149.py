# Generated by Django 2.2.4 on 2020-05-25 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_wallpaper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='cadence',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Weekly'), (1, 'Monthly'), (2, 'Every Two Weeks'), (3, 'Every Two Months'), (4, 'Every Three Months')]),
        ),
    ]
