# Generated by Django 3.2.9 on 2022-10-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffersCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='orderdetails',
            options={'verbose_name_plural': 'Order Details'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='storemenu',
            options={'verbose_name_plural': 'Store Menu'},
        ),
        migrations.AlterModelOptions(
            name='stores',
            options={'verbose_name_plural': 'Stores'},
        ),
    ]