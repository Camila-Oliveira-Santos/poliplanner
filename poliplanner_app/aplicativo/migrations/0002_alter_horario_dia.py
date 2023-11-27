from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("aplicativo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="horario",
            name="dia",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="aplicativo.dia",
            ),
        ),
    ]
