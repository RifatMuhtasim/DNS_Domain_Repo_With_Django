# Generated by Django 3.2.6 on 2021-09-03 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DomainSearch', '0003_auto_20210903_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dnstlds',
            old_name='DnsTlds',
            new_name='DnsTldsName',
        ),
    ]
