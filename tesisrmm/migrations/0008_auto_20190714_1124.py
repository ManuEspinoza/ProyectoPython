# Generated by Django 2.2.1 on 2019-07-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesisrmm', '0007_auto_20190714_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesis',
            name='fecha',
            field=models.DateTimeField(verbose_name='fecha de publicación'),
        ),
    ]