# Generated by Django 2.2 on 2020-11-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiative', '0003_auto_20201106_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
