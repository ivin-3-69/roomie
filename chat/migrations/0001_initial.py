# Generated by Django 3.1.4 on 2021-01-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chatdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('time_match', models.DateTimeField(auto_now_add=True)),
                ('message_last', models.CharField(max_length=200)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]