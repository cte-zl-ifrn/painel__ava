# Generated by Django 4.0.5 on 2022-06-14 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_alter_ambiente_sigla_alter_diario_codigo'),
        ('middleware', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.campus'),
        ),
    ]