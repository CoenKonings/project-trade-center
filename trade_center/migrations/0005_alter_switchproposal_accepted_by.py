# Generated by Django 4.2.7 on 2023-11-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_center', '0004_alter_switchproposal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switchproposal',
            name='accepted_by',
            field=models.ManyToManyField(blank=True, to='trade_center.switchproposal'),
        ),
    ]