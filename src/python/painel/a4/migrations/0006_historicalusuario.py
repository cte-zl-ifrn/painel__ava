# Generated by Django 4.2.3 on 2023-08-01 16:43

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):
    dependencies = [
        ("painel", "0010_alter_historicalvinculocurso_colaborador_and_more"),
        ("a4", "0005_alter_grupo_managers_alter_usuario_managers_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalUsuario",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        db_index=True,
                        error_messages={
                            "unique": "A user with that IFRN-id already exists."
                        },
                        max_length=150,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="IFRN-id",
                    ),
                ),
                (
                    "nome_registro",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="nome civil"
                    ),
                ),
                (
                    "nome_social",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="nome social",
                    ),
                ),
                (
                    "nome_usual",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="nome de apresentação",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="nome no SUAP",
                    ),
                ),
                (
                    "tipo_usuario",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Servidor (Docente)", "Servidor (Docente)"),
                            (
                                "Servidor (Técnico-Administrativo)",
                                "Servidor (Técnico-Administrativo)",
                            ),
                            ("Prestador de Serviço", "Prestador de Serviço"),
                            ("Aluno", "Aluno"),
                            ("desconhecido", "Desconhecido"),
                        ],
                        max_length=255,
                        null=True,
                        verbose_name="tipo",
                    ),
                ),
                (
                    "foto",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="URL da foto",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, null=True, verbose_name="e-Mail preferêncial"
                    ),
                ),
                (
                    "email_secundario",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="e-Mail pessoal",
                    ),
                ),
                (
                    "email_corporativo",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="e-Mail corporativo",
                    ),
                ),
                (
                    "email_google_classroom",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="e-Mail Gogole Classroom",
                    ),
                ),
                (
                    "email_academico",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="e-Mail academico",
                    ),
                ),
                (
                    "first_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="first login"
                    ),
                ),
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
                    "campus",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="painel.campus",
                        verbose_name="campus do aluno",
                    ),
                ),
                (
                    "curso",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="painel.curso",
                        verbose_name="curso do aluno",
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
                (
                    "polo",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="painel.polo",
                        verbose_name="pólo do aluno",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical usuário",
                "verbose_name_plural": "historical usuários",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
