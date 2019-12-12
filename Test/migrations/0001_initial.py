# Generated by Django 2.0.13 on 2019-12-12 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.CharField(blank=True, max_length=254, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('surname', models.CharField(blank=True, max_length=254, null=True)),
                ('login', models.CharField(max_length=254, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.Product'),
        ),
    ]
