# Generated by Django 5.1.1 on 2024-12-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_appdetails_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='AppDetails',
        ),
    ]
