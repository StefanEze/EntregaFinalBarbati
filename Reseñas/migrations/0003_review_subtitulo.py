# Generated by Django 4.1.7 on 2023-04-03 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reseñas', '0002_review_imagen_portada_alter_review_cuerpo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='subtitulo',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
    ]
