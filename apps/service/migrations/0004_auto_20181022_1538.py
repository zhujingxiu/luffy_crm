# Generated by Django 2.0.6 on 2018-10-22 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20181019_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(blank=True, limit_choices_to={'depart__code': 'marketing'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultant', to='system.UserInfo', verbose_name='课程顾问'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='course',
            field=models.ManyToManyField(related_name='courses', to='system.Course', verbose_name='咨询课程'),
        ),
    ]
