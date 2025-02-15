# Generated by Django 3.2.19 on 2023-06-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_article_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(blank=True, choices=[('change-submitted', 'Change submitted'), ('required-update', 'Required update'), ('required-erratum', 'Required erratum'), ('read-to-publish', 'Ready to publish'), ('scheduled-to-publish', 'Scheduled to publish'), ('published', 'Publicado')], max_length=32, null=True, verbose_name='Article status'),
        ),
    ]
