# Generated by Django 4.2.3 on 2023-09-01 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_subcategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.subcategoria'),
        ),
    ]
