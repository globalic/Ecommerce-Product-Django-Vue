# Generated by Django 2.2 on 2019-05-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childproduct', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childproduct',
            name='is_main',
            field=models.BooleanField(default=False, help_text="Should we display these details                                   as main product's details ? <br><b>Note :                                  one product should be set as main</b>"),
        ),
    ]
