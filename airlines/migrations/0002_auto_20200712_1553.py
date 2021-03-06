# Generated by Django 3.0.8 on 2020-07-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_history',
            name='from_place',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking_history',
            name='seat_no',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking_history',
            name='to_place',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
