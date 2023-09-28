# Generated by Django 3.2.20 on 2023-09-15 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0058_jobresult_add_time_status_idxs"),
        ("nautobot_golden_config", "0026_configplan"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="remediationsetting",
            options={"ordering": ("platform", "remediation_type")},
        ),
        migrations.RenameField(
            model_name="configplan",
            old_name="job_result",
            new_name="plan_result",
        ),
        migrations.AddField(
            model_name="configplan",
            name="deploy_result",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="config_plan_deploy_result",
                to="extras.jobresult",
            ),
        ),
        migrations.AlterField(
            model_name="configplan",
            name="change_control_id",
            field=models.CharField(blank=True, default="", max_length=50),
            preserve_default=False,
        ),
    ]