# Generated by Django 3.0.6 on 2020-05-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='elevenclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='class11/videos')),
            ],
        ),
        migrations.CreateModel(
            name='twelveclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='class12/videos')),
            ],
        ),
    ]