# Generated by Django 4.0.4 on 2022-05-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_noticia_pag_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='category',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
    ]
