# Generated by Django 3.1.8 on 2021-05-16 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.UUIDField(unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('initial_balance', models.PositiveIntegerField()),
                ('postal_code', models.PositiveIntegerField()),
                ('account_type', models.CharField(max_length=24)),
                ('current_balance', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
