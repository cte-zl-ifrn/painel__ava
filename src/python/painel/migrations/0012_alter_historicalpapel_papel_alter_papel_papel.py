# Generated by Django 4.2.4 on 2023-08-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("painel", "0011_historicalpapel_papel_papel_papel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpapel",
            name="papel",
            field=models.CharField(db_index=True, max_length=256, verbose_name="papel"),
        ),
        migrations.AlterField(
            model_name="papel",
            name="papel",
            field=models.CharField(max_length=256, unique=True, verbose_name="papel"),
        ),
    ]
