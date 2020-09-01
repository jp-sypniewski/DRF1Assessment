# Generated by Django 3.1 on 2020-08-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('company_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=120)),
                ('job_description', models.CharField(max_length=120)),
                ('salary', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
