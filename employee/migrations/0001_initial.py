# Generated by Django 4.2.6 on 2023-10-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('position', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
