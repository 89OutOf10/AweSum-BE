# Generated by Django 3.2.13 on 2022-05-03 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_merge_20220504_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtitle',
            old_name='video',
            new_name='videoid',
        ),
    ]