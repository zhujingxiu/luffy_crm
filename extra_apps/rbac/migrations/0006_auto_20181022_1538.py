# Generated by Django 2.0.6 on 2018-10-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_role_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='permissions', to='rbac.Permission', verbose_name='拥有的所有权限'),
        ),
    ]
