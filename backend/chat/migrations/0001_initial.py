# Generated by Django 3.2.11 on 2022-01-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('port', models.IntegerField(null=True)),
                ('pkey', models.TextField(null=True)),
            ],
        ),
    ]
