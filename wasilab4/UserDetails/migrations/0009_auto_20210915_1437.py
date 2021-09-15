# Generated by Django 3.2.6 on 2021-09-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0008_auto_20210915_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnsinformation',
            name='DnsStatus',
            field=models.CharField(blank=True, default='No', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dnsinformation',
            name='DomainAutoRenew',
            field=models.CharField(blank=True, default='No', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dnsinformation',
            name='DomainPremium',
            field=models.CharField(blank=True, default='No', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dnsinformation',
            name='DomainSsl',
            field=models.CharField(blank=True, default='No', max_length=50, null=True),
        ),
    ]