# Generated by Django 2.2.15 on 2020-08-31 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
