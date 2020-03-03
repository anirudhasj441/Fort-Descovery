# Generated by Django 3.0.3 on 2020-03-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desc', models.TextField(max_length=3000, null=True)),
                ('image', models.ImageField(null=True, upload_to='app/images')),
            ],
            options={
                'verbose_name': 'Fort',
                'verbose_name_plural': 'Forts',
            },
        ),
    ]