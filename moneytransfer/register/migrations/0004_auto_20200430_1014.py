# Generated by Django 3.0.5 on 2020-04-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_userprofile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
