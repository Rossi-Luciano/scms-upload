# Generated by Django 3.2.12 on 2022-09-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(blank=True, choices=[('required-correction', 'Required correction'), ('required-erratum', 'Required erratum'), ('published', 'Publicado')], max_length=32, null=True, verbose_name='Article status'),
        ),
        migrations.AlterField(
            model_name='requestarticlechange',
            name='change_type',
            field=models.CharField(choices=[('correction', 'Correction'), ('erratum', 'Erratum')], max_length=32, verbose_name='Change type'),
        ),
    ]
