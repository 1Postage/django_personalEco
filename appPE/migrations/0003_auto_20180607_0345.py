# Generated by Django 2.2.dev20180601101617 on 2018-06-07 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPE', '0002_auto_20180605_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='fecha_hora',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='gasto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='fecha_hora',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
