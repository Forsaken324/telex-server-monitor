# Generated by Django 5.2 on 2025-04-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
            ],
        ),
    ]
