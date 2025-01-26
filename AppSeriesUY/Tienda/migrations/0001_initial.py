# Generated by Django 5.1.4 on 2025-01-26 19:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('vendedor', models.CharField(default='Autor', max_length=100)),
                ('descripcion', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='feed_images')),
            ],
        ),
    ]
