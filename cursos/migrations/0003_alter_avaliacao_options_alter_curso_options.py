# Generated by Django 5.0.7 on 2024-07-30 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_avaliacao_options_rename_ativa_avaliacao_ativo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'ordering': ['id'], 'verbose_name': 'Avaliação', 'verbose_name_plural': 'Avaliações'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['id'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]
