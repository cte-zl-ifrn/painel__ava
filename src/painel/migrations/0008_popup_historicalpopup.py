# Generated by Django 4.2.3 on 2023-07-27 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models
import painel.models
import simple_history.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("painel", "0007_remove_ambiente_cor_remove_historicalambiente_cor_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Popup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("titulo", models.CharField(max_length=256, verbose_name="título")),
                ("url", models.URLField(max_length=256, verbose_name="url")),
                (
                    "mensagem",
                    djrichtextfield.models.RichTextField(verbose_name="mensagem"),
                ),
                ("start_at", models.DateTimeField(verbose_name="inicia em")),
                ("end_at", models.DateTimeField(verbose_name="termina em")),
                ("active", models.BooleanField(verbose_name="ativo?")),
            ],
            options={
                "verbose_name": "popup",
                "verbose_name_plural": "popups",
                "ordering": ["start_at", "titulo"],
            },
            bases=(painel.models.ActiveMixin, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalPopup",
            fields=[
                (
                    "id",
                    models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID"),
                ),
                (
                    "deleted",
                    models.DateTimeField(db_index=True, editable=False, null=True),
                ),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                ("titulo", models.CharField(max_length=256, verbose_name="título")),
                ("url", models.URLField(max_length=256, verbose_name="url")),
                (
                    "mensagem",
                    djrichtextfield.models.RichTextField(verbose_name="mensagem"),
                ),
                ("start_at", models.DateTimeField(verbose_name="inicia em")),
                ("end_at", models.DateTimeField(verbose_name="termina em")),
                ("active", models.BooleanField(verbose_name="ativo?")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical popup",
                "verbose_name_plural": "historical popups",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
