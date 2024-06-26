# Generated by Django 4.0 on 2024-03-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_widget_is_deleted_alter_widget_is_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_feature_page',
            name='container_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='report_feature_page',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='report_feature_page',
            name='created_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='report_feature_page',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='report_feature_page',
            name='updated_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='report_page',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='report_page',
            name='created_dt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='report_page',
            name='definition',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='report_page',
            name='update_dt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='report_page',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='container_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='created_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='updated_date',
            field=models.DateTimeField(null=True),
        ),
    ]
