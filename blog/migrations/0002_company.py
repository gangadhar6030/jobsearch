# Generated by Django 2.2.7 on 2021-01-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobposition', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=30)),
                ('jobdescription', models.TextField()),
                ('requiredskills', models.TextField()),
            ],
        ),
    ]
