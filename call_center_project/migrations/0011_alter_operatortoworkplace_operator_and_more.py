# Generated by Django 4.1.7 on 2023-04-25 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('call_center_project', '0010_alter_calllog_response_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatortoworkplace',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='operatortoworkplace',
            name='work_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call_center_project.workplace'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='operators',
            field=models.ManyToManyField(related_name='work_place', through='call_center_project.OperatorToWorkPlace', to=settings.AUTH_USER_MODEL),
        ),
    ]
