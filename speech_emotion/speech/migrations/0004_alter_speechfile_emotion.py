# Generated by Django 4.2.2 on 2023-06-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0003_auto_20230606_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechfile',
            name='emotion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
