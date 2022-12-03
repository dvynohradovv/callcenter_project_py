# Generated by Django 4.1.3 on 2022-12-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_center_project', '0004_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('Unactive', 'Unactive'), ('Admin', 'Admin'), ('Operator', 'Operator'), ('TenantCompanyOwner', 'Tenantcompanyowner')], default='Unactive', max_length=100),
        ),
    ]
