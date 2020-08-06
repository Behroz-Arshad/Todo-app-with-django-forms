# Generated by Django 3.0.7 on 2020-06-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Complete', models.BooleanField(default=False)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
