# Generated by Django 2.1.7 on 2019-03-31 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('howdy', '0003_auto_20190401_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Person_name',
            new_name='name',
        ),
    ]