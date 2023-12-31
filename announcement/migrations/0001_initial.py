# Generated by Django 5.0 on 2023-12-31 15:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('ano', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('valor', models.FloatField()),
                ('km', models.FloatField()),
                ('placa', models.CharField(max_length=7)),
                ('transmissao', models.CharField(choices=[('M', 'Manual'), ('A', 'Automático')], max_length=1)),
                ('cor', models.CharField(max_length=10)),
                ('descricao', models.TextField(max_length=600)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='announcement.announcement')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
