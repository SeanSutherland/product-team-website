# Generated by Django 3.2.9 on 2021-11-27 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0004_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_suffix',
            field=models.CharField(default='default', max_length=120),
            preserve_default=False,
        ),
    ]
