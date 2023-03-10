# Generated by Django 4.0.3 on 2022-12-29 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('client_phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_boss_name', models.CharField(max_length=200)),
                ('company_phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=200)),
                ('p_price', models.IntegerField()),
                ('p_registerdate', models.DateTimeField()),
                ('p_company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmsoft.company')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_date', models.DateTimeField()),
                ('o_number', models.IntegerField()),
                ('o_client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmsoft.client')),
                ('o_p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmsoft.product')),
            ],
        ),
    ]
