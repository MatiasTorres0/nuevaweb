# Generated by Django 4.2.3 on 2023-08-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_categoria_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='cantidad_productos',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
